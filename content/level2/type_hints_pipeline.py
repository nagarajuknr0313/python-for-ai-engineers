"""A type-hinted example for AI pipeline payloads."""

from __future__ import annotations


def build_typed_request(task: str, context: str) -> dict[str, str]:
    """Create a typed request payload for an AI pipeline."""
    return {"task": task, "context": context}


if __name__ == "__main__":
    print(build_typed_request("summarize", "support"))
