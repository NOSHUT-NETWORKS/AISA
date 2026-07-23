"""In-memory session management for the local First Boot application."""

from __future__ import annotations

from dataclasses import dataclass
from threading import Lock
from uuid import uuid4

from .models import ConsultationContext


@dataclass
class ConsultationSession:
    session_id: str
    context: ConsultationContext


class SessionManager:
    def __init__(self) -> None:
        self._sessions: dict[str, ConsultationSession] = {}
        self._lock = Lock()

    def create(self) -> ConsultationSession:
        with self._lock:
            session_id = uuid4().hex
            session = ConsultationSession(
                session_id=session_id,
                context=ConsultationContext(session_id=session_id),
            )
            self._sessions[session_id] = session
            return session

    def get(self, session_id: str) -> ConsultationSession:
        try:
            return self._sessions[session_id]
        except KeyError as exc:
            raise KeyError(f"Unknown session: {session_id}") from exc

    def restart(self, session_id: str) -> ConsultationSession:
        with self._lock:
            session = self.get(session_id)
            session.context = ConsultationContext(session_id=session_id)
            return session
