"""Dependency-free local HTTP application for AISA First Boot."""

from __future__ import annotations

import argparse
import json
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from .navigation import AnswerValidationError
from .service import ConsultationService


STATIC_DIR = Path(__file__).with_name("static")


class AISARequestHandler(BaseHTTPRequestHandler):
    service = ConsultationService()

    def log_message(self, format: str, *args: Any) -> None:
        print(f"[AISA] {self.address_string()} - {format % args}")

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/":
            self._serve_file(STATIC_DIR / "index.html")
            return
        if path.startswith("/static/"):
            candidate = (STATIC_DIR / path.removeprefix("/static/")).resolve()
            if STATIC_DIR.resolve() not in candidate.parents:
                self._json_error(HTTPStatus.NOT_FOUND, "Not found")
                return
            self._serve_file(candidate)
            return
        if path.startswith("/api/sessions/"):
            session_id = path.removeprefix("/api/sessions/")
            self._call_service(
                lambda: self.service.get_state(session_id)
            )
            return
        self._json_error(HTTPStatus.NOT_FOUND, "Not found")

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/sessions":
            self._call_service(self.service.start, HTTPStatus.CREATED)
            return
        parts = path.strip("/").split("/")
        if len(parts) == 4 and parts[:2] == ["api", "sessions"]:
            session_id, action = parts[2], parts[3]
            if action == "answers":
                payload = self._read_json()
                if payload is None:
                    return
                self._call_service(
                    lambda: self.service.answer(
                        session_id,
                        str(payload.get("question_id", "")),
                        str(payload.get("value", "")),
                    )
                )
                return
            if action == "restart":
                self._call_service(
                    lambda: self.service.restart(session_id)
                )
                return
        self._json_error(HTTPStatus.NOT_FOUND, "Not found")

    def _call_service(
        self,
        operation: Any,
        status: HTTPStatus = HTTPStatus.OK,
    ) -> None:
        try:
            result = operation()
        except (KeyError, AnswerValidationError) as exc:
            self._json_error(HTTPStatus.BAD_REQUEST, str(exc))
            return
        self._send_json(status, result)

    def _read_json(self) -> dict[str, Any] | None:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(
                self.rfile.read(content_length).decode("utf-8")
            )
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
            self._json_error(
                HTTPStatus.BAD_REQUEST, "Request body must be valid JSON"
            )
            return None
        if not isinstance(payload, dict):
            self._json_error(
                HTTPStatus.BAD_REQUEST, "JSON body must be an object"
            )
            return None
        return payload

    def _serve_file(self, path: Path) -> None:
        if not path.is_file():
            self._json_error(HTTPStatus.NOT_FOUND, "Not found")
            return
        content_type = mimetypes.guess_type(path.name)[0] or "text/plain"
        body = path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status: HTTPStatus, payload: Any) -> None:
        body = json.dumps(
            payload, ensure_ascii=False, separators=(",", ":")
        ).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json_error(self, status: HTTPStatus, message: str) -> None:
        self._send_json(status, {"error": message})


def create_server(
    host: str = "127.0.0.1", port: int = 8000
) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), AISARequestHandler)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run AISA First Boot")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    args = parser.parse_args()
    server = create_server(args.host, args.port)
    print(f"AISA First Boot: http://{args.host}:{server.server_port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping AISA.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
