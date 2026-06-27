"""A small memory example for conversational AI.

Conversation memory helps an agent keep track of earlier turns in a chat.
This example stores a simple history of messages.
"""

from __future__ import annotations


def build_memory(turns: list[dict[str, str]]) -> list[dict[str, str]]:
    """Keep a compact conversation memory for an agent."""
    return turns


if __name__ == "__main__":
    history = [{"speaker": "user", "text": "Summarize the release plan"}]
    print(build_memory(history))
