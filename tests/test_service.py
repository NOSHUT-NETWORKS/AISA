import unittest

from aisa.service import ConsultationService


class ConsultationServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.service = ConsultationService()

    def _complete(
        self, answers: list[tuple[str, str]]
    ) -> dict:
        state = self.service.start()
        session_id = state["session_id"]
        for question_id, value in answers:
            state = self.service.answer(
                session_id, question_id, value
            )
        return state

    def test_successful_end_to_end_flow(self) -> None:
        state = self._complete(
            [
                ("Q-PURPOSE-001", "automation"),
                ("Q-TOOLS-001", "word"),
                (
                    "Q-PROBLEM-001",
                    "repetitive_document_creation",
                ),
                ("Q-PRIORITY-001", "time"),
            ]
        )

        self.assertEqual("diagnosis", state["status"])
        self.assertEqual(
            "AKE-DOC-001", state["report"]["pattern_id"]
        )
        self.assertEqual(
            "unanswered", state["context"]["budget_level"]
        )

    def test_knowledge_unknown_flow(self) -> None:
        state = self._complete(
            [
                ("Q-PURPOSE-001", "comparison"),
                ("Q-TOOLS-001", "other"),
                ("Q-PROBLEM-001", "slow_inquiry_response"),
                ("Q-PRIORITY-001", "ai"),
            ]
        )

        self.assertEqual("knowledge_unknown", state["status"])
        self.assertIn(
            "AKE Registration", state["report"]["unknown_route"]
        )

    def test_restart_clears_context_and_returns_first_question(self) -> None:
        state = self.service.start()
        session_id = state["session_id"]
        self.service.answer(
            session_id, "Q-PURPOSE-001", "automation"
        )

        restarted = self.service.restart(session_id)

        self.assertEqual("question", restarted["status"])
        self.assertEqual(
            "Q-PURPOSE-001",
            restarted["question"]["question_id"],
        )
        self.assertEqual(
            "unanswered", restarted["context"]["purpose"]
        )


if __name__ == "__main__":
    unittest.main()
