"""A simple class-based AI agent example.

Classes help group related behavior. In this example, the agent stores a
role and provides a method to answer a support-related task.
"""

from __future__ import annotations


class SupportAgent:
    """A compact agent that stores a role and answers tasks."""

    def __init__(self, role: str) -> None:
        # The role describes the agent's purpose.
        self.role = role

    def answer(self, task: str) -> str:
        """Return a short response for a task."""
        return f"{self.role}: I can help with {task}"


if __name__ == "__main__":
    agent = SupportAgent("policy-assistant")
    response = agent.answer("ticket triage")
    print(response)
