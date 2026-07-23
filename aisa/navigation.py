"""Rule-based Consultation Navigator."""

from __future__ import annotations

from typing import Any

from .models import ConsultationContext


class AnswerValidationError(ValueError):
    """Raised when an answer is outside the Question Catalog."""


class ConsultationNavigator:
    def __init__(
        self,
        questions: list[dict[str, Any]],
        navigation_rules: list[dict[str, Any]],
    ) -> None:
        self.questions = {item["question_id"]: item for item in questions}
        self.navigation_rules = navigation_rules

    def get_question(self, question_id: str) -> dict[str, Any]:
        try:
            return self.questions[question_id]
        except KeyError as exc:
            raise KeyError(f"Unknown question: {question_id}") from exc

    def next_question(
        self, context: ConsultationContext
    ) -> dict[str, Any] | None:
        for rule in self.navigation_rules:
            question = self.get_question(rule["question_id"])
            if context.is_answered(question["context_field"]):
                continue
            required_answers = rule.get("when", {}).get("answered", [])
            if all(context.is_answered(name) for name in required_answers):
                return question
        return None

    def record_answer(
        self,
        context: ConsultationContext,
        question_id: str,
        value: str,
    ) -> None:
        question = self.get_question(question_id)
        allowed_values = {option["value"] for option in question["options"]}
        if value not in allowed_values:
            raise AnswerValidationError(
                f"{value!r} is not valid for {question_id}"
            )
        context.set_answer(question["context_field"], value)

    def is_complete(self, context: ConsultationContext) -> bool:
        required_fields = {
            question["context_field"]
            for question in self.questions.values()
            if question.get("required", False)
        }
        return all(context.is_answered(name) for name in required_fields)
