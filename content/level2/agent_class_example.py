"""A simple class-based AI agent example."""

from __future__ import annotations


class SupportAgent:
    """A compact agent that stores a role and answers tasks."""

    def __init__(self, role: str) -> None:
        self.role = role

    def answer(self, task: str) -> str:
        """Return a short response for a task."""
        return f"{self.role}: I can help with {task}"


if __name__ == "__main__":
    agent = SupportAgent("policy-assistant")
    print(agent.answer("ticket triage"))
