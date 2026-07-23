"""AKE-first, rule-based Recommendation Engine."""

from __future__ import annotations

from typing import Any

from .models import ConsultationContext, DiagnosisReport


UNKNOWN_ROUTE = [
    "Engineering Analysis",
    "Human Review",
    "AKE Registration",
    "Future Automatic Diagnosis",
]


class RecommendationEngine:
    """Evaluate AKE patterns without owning business knowledge."""

    def __init__(self, patterns: list[dict[str, Any]]) -> None:
        self.patterns = patterns

    @staticmethod
    def _matches(
        pattern: dict[str, Any], context: ConsultationContext
    ) -> bool:
        conditions = pattern.get("applicable_conditions", {})
        return all(
            context.answers.get(field_name) == expected
            for field_name, expected in conditions.items()
        )

    def diagnose(self, context: ConsultationContext) -> DiagnosisReport:
        candidates = [
            pattern
            for pattern in self.patterns
            if self._matches(pattern, context)
        ]
        if not candidates:
            return DiagnosisReport(
                status="knowledge_unknown",
                context=context.as_dict(),
                reason=(
                    "Consultation Context is complete, but AKE has no "
                    "sufficient Diagnostic Pattern."
                ),
                unknown_route=UNKNOWN_ROUTE,
            )

        pattern = max(
            candidates,
            key=lambda item: (
                item.get("success_probability", 0),
                len(item.get("applicable_conditions", {})),
            ),
        )
        priority = context.answers["priority"]
        first_actions = pattern.get("first_actions", {})
        return DiagnosisReport(
            status="diagnosis",
            context=context.as_dict(),
            pattern_id=pattern["pattern_id"],
            title=pattern["title"],
            summary=pattern["summary"],
            recommendations=pattern["recommendations"],
            first_action=first_actions.get(
                priority, pattern["default_first_action"]
            ),
        )
