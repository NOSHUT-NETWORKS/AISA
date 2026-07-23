import unittest

from aisa.catalog import load_patterns
from aisa.models import ConsultationContext
from aisa.recommendation import RecommendationEngine


class RecommendationEngineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = RecommendationEngine(load_patterns())

    def test_known_context_generates_diagnosis_report(self) -> None:
        context = ConsultationContext(session_id="known")
        context.answers.update(
            {
                "purpose": "automation",
                "current_tool": "word",
                "main_problem": "repetitive_document_creation",
                "priority": "cost",
            }
        )

        report = self.engine.diagnose(context)

        self.assertEqual("diagnosis", report.status)
        self.assertEqual("AKE-DOC-001", report.pattern_id)
        self.assertIn("Word", report.summary)
        self.assertTrue(report.first_action)
        self.assertEqual(
            {"cost", "time", "ai"}, set(report.recommendations)
        )

    def test_unknown_context_enters_unknown_route(self) -> None:
        context = ConsultationContext(session_id="unknown")
        context.answers.update(
            {
                "purpose": "quality",
                "current_tool": "teams",
                "main_problem": "slow_approval",
                "priority": "time",
            }
        )

        report = self.engine.diagnose(context)

        self.assertEqual("knowledge_unknown", report.status)
        self.assertEqual("Engineering Analysis", report.unknown_route[0])
        self.assertIn("AKE Registration", report.unknown_route)


if __name__ == "__main__":
    unittest.main()
