"""A simple class-based AI agent example for beginners."""

from __future__ import annotations


class PlanningAgent:
    """A minimal agent that prepares an action plan."""

    def __init__(self, role: str) -> None:
        self.role = role

    def plan(self, goal: str) -> list[str]:
        """Return a short plan for a goal."""
        return [f"Inspect {goal}", "Break the task into steps", "Share the plan"]


if __name__ == "__main__":
    agent = PlanningAgent("research-agent")
    print(agent.plan("new model launch"))
