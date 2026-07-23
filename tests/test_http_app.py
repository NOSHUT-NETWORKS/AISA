import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from aisa.app import AISARequestHandler, create_server
from aisa.service import ConsultationService


class HTTPApplicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        AISARequestHandler.service = ConsultationService()
        cls.server = create_server(port=0)
        cls.thread = threading.Thread(
            target=cls.server.serve_forever, daemon=True
        )
        cls.thread.start()
        cls.base_url = (
            f"http://127.0.0.1:{cls.server.server_port}"
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def _request(
        self, path: str, method: str = "GET", payload: dict | None = None
    ) -> tuple[int, dict]:
        body = (
            json.dumps(payload).encode("utf-8")
            if payload is not None
            else None
        )
        request = Request(
            self.base_url + path,
            data=body,
            method=method,
            headers={"Content-Type": "application/json"},
        )
        with urlopen(request, timeout=3) as response:
            return response.status, json.loads(response.read())

    def test_session_api_starts_and_restarts(self) -> None:
        status, started = self._request(
            "/api/sessions", "POST", {}
        )
        self.assertEqual(201, status)
        self.assertEqual("Q-PURPOSE-001", started["question"]["question_id"])

        _, restarted = self._request(
            f"/api/sessions/{started['session_id']}/restart",
            "POST",
            {},
        )
        self.assertEqual("question", restarted["status"])

    def test_first_light_landing_page(self) -> None:
        with urlopen(self.base_url + "/", timeout=3) as response:
            body = response.read().decode("utf-8")

        self.assertEqual(200, response.status)
        self.assertIn("<h1>AISA</h1>", body)
        self.assertIn("AI Solution Architect", body)
        self.assertIn("Version 0.0.1", body)
        self.assertIn("Vertical Slice 0", body)
        self.assertIn("Start Consultation", body)

    def test_invalid_answer_returns_bad_request(self) -> None:
        _, started = self._request("/api/sessions", "POST", {})
        with self.assertRaises(HTTPError) as error:
            self._request(
                f"/api/sessions/{started['session_id']}/answers",
                "POST",
                {
                    "question_id": "Q-PURPOSE-001",
                    "value": "free_text",
                },
            )
        self.assertEqual(400, error.exception.code)


if __name__ == "__main__":
    unittest.main()
