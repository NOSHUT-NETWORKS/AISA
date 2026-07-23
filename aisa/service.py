"""Application service that connects navigation, sessions, and diagnosis."""

from __future__ import annotations

from typing import Any

from .catalog import (
    load_navigation_rules,
    load_patterns,
    load_questions,
)
from .navigation import ConsultationNavigator
from .recommendation import RecommendationEngine
from .session import SessionManager


class ConsultationService:
    def __init__(self) -> None:
        self.navigator = ConsultationNavigator(
            load_questions(), load_navigation_rules()
        )
        self.recommendation_engine = RecommendationEngine(load_patterns())
        self.sessions = SessionManager()

    def start(self) -> dict[str, Any]:
        session = self.sessions.create()
        return self._state(session.session_id)

    def get_state(self, session_id: str) -> dict[str, Any]:
        self.sessions.get(session_id)
        return self._state(session_id)

    def answer(
        self, session_id: str, question_id: str, value: str
    ) -> dict[str, Any]:
        session = self.sessions.get(session_id)
        self.navigator.record_answer(
            session.context, question_id, value
        )
        return self._state(session_id)

    def restart(self, session_id: str) -> dict[str, Any]:
        self.sessions.restart(session_id)
        return self._state(session_id)

    def _state(self, session_id: str) -> dict[str, Any]:
        session = self.sessions.get(session_id)
        question = self.navigator.next_question(session.context)
        base = {
            "session_id": session_id,
            "context": session.context.as_dict(),
        }
        if question is not None:
            return {
                **base,
                "status": "question",
                "question": question,
            }
        if not self.navigator.is_complete(session.context):
            return {
                **base,
                "status": "information_unknown",
                "reason": "Required consultation information is missing.",
            }
        report = self.recommendation_engine.diagnose(session.context)
        return {
            **base,
            "status": report.status,
            "report": report.as_dict(),
        }
