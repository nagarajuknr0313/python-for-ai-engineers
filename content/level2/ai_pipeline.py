"""Intermediate Python example for an AI evaluation pipeline."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterator


class ApiFailure(Exception):
    """Raised when an AI service call fails."""


def load_evaluation_rows(path: str) -> list[dict[str, str]]:
    """Load evaluation rows from a CSV file."""
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def save_llm_response(path: str, payload: dict[str, object]) -> None:
    """Save a response payload to a JSON file."""
    output_path = Path(path)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def stream_tokens(text: str) -> Iterator[str]:
    """Yield tokens from a text string one by one."""
    for token in text.split():
        yield token


def process_case(row: dict[str, str]) -> dict[str, str]:
    """Prepare a single evaluation case for analysis."""
    if not row.get("prompt"):
        raise ApiFailure("Prompt is missing")

    return {
        "prompt": row["prompt"],
        "expected_label": row.get("expected_label", "unknown"),
    }


if __name__ == "__main__":
    rows = load_evaluation_rows("content/level2/sample_evaluations.csv")
    processed = [process_case(row) for row in rows]
    save_llm_response("content/level2/processed_cases.json", {"cases": processed})

    for token in stream_tokens("research assistant streaming tokens"):
        print(token)
