"""Domain models for the IWP-0001 consultation flow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


UNANSWERED = "unanswered"


@dataclass
class ConsultationContext:
    """Standardized input passed from navigation to recommendation."""

    session_id: str
    answers: dict[str, str] = field(
        default_factory=lambda: {
            "purpose": UNANSWERED,
            "current_tool": UNANSWERED,
            "main_problem": UNANSWERED,
            "priority": UNANSWERED,
            "approval_required": UNANSWERED,
            "budget_level": UNANSWERED,
            "security_level": UNANSWERED,
        }
    )

    def set_answer(self, field_name: str, value: str) -> None:
        if field_name not in self.answers:
            raise KeyError(f"Unknown context field: {field_name}")
        self.answers[field_name] = value

    def is_answered(self, field_name: str) -> bool:
        return self.answers.get(field_name, UNANSWERED) != UNANSWERED

    def as_dict(self) -> dict[str, str]:
        return dict(self.answers)


@dataclass(frozen=True)
class DiagnosisReport:
    status: str
    context: dict[str, str]
    pattern_id: str | None = None
    title: str | None = None
    summary: str | None = None
    recommendations: dict[str, str] = field(default_factory=dict)
    first_action: str | None = None
    reason: str | None = None
    unknown_route: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "context": self.context,
            "pattern_id": self.pattern_id,
            "title": self.title,
            "summary": self.summary,
            "recommendations": self.recommendations,
            "first_action": self.first_action,
            "reason": self.reason,
            "unknown_route": self.unknown_route,
        }
