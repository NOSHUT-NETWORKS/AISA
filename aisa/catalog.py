"""Load the small, file-backed AKE catalog used by Vertical Slice 0."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).with_name("data")


def _load_json(filename: str) -> list[dict[str, Any]]:
    with (DATA_DIR / filename).open(encoding="utf-8") as source:
        data = json.load(source)
    if not isinstance(data, list):
        raise ValueError(f"{filename} must contain a JSON array")
    return data


def load_questions() -> list[dict[str, Any]]:
    return _load_json("questions.json")


def load_navigation_rules() -> list[dict[str, Any]]:
    return _load_json("navigation_rules.json")


def load_patterns() -> list[dict[str, Any]]:
    return _load_json("diagnostic_patterns.json")
