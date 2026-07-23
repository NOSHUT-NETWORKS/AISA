import unittest

from aisa.catalog import load_navigation_rules, load_questions
from aisa.models import ConsultationContext
from aisa.navigation import AnswerValidationError, ConsultationNavigator


class ConsultationNavigatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.navigator = ConsultationNavigator(
            load_questions(), load_navigation_rules()
        )
        self.context = ConsultationContext(session_id="test")

    def test_questions_follow_navigation_rules(self) -> None:
        expected = [
            ("Q-PURPOSE-001", "automation"),
            ("Q-TOOLS-001", "word"),
            ("Q-PROBLEM-001", "repetitive_document_creation"),
            ("Q-PRIORITY-001", "cost"),
        ]
        for question_id, value in expected:
            question = self.navigator.next_question(self.context)
            self.assertIsNotNone(question)
            self.assertEqual(question_id, question["question_id"])
            self.navigator.record_answer(
                self.context, question_id, value
            )

        self.assertIsNone(self.navigator.next_question(self.context))
        self.assertTrue(self.navigator.is_complete(self.context))

    def test_invalid_choice_is_rejected(self) -> None:
        with self.assertRaises(AnswerValidationError):
            self.navigator.record_answer(
                self.context, "Q-PURPOSE-001", "free_text"
            )

    def test_optional_fields_remain_unanswered(self) -> None:
        self.assertEqual(
            "unanswered", self.context.answers["budget_level"]
        )
        self.assertEqual(
            "unanswered", self.context.answers["security_level"]
        )


if __name__ == "__main__":
    unittest.main()
