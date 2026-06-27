"""A list-based representation of chat history for a support copilot."""

from __future__ import annotations


def build_chat_history() -> list[dict[str, str]]:
    """Create a short chat history transcript."""
    return [
        {"speaker": "user", "text": "I need help with invoice billing."},
        {"speaker": "assistant", "text": "I can explain the invoice steps."},
    ]


if __name__ == "__main__":
    for turn in build_chat_history():
        print(turn["speaker"], ":", turn["text"])
