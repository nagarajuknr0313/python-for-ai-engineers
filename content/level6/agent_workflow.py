"""Simple planning agent workflow for AI engineering tasks."""

from __future__ import annotations


class PlannerAgent:
    """Create a short plan for a user request."""

    def plan(self, task: str) -> list[str]:
        """Split a task into a small set of planning steps."""
        words = task.split()
        if not words:
            return []
        return [
            f"Inspect the context for: {task}",
            "Identify the key constraints",
            "Draft a concise action plan",
        ]


if __name__ == "__main__":
    agent = PlannerAgent()
    print(agent.plan("research the new model launch"))
