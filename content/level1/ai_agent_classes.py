"""A simple class-based AI agent example for beginners.

Classes let us model real-world concepts with data and behavior. Here, a
planning agent has a role and a method that produces a simple plan.
"""

from __future__ import annotations


class PlanningAgent:
    """A minimal agent that prepares an action plan."""

    def __init__(self, role: str) -> None:
        # Store the agent's role so it can describe its behavior.
        self.role = role

    def plan(self, goal: str) -> list[str]:
        """Return a short plan for a goal."""
        return [
            f"Inspect {goal}",
            "Break the task into steps",
            "Share the plan with the team",
        ]


if __name__ == "__main__":
    agent = PlanningAgent("research-agent")
    plan = agent.plan("new model launch")
    print(f"{agent.role} plan: {plan}")
