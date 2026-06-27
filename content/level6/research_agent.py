"""A simple research agent example.

This agent demonstrates how object-oriented design can model a basic workflow
for gathering information and turning it into a short plan.
"""

from __future__ import annotations


class ResearchAgent:
    """Create a basic research plan for a topic."""

    def plan(self, topic: str) -> list[str]:
        """Return a short research plan."""
        return [
            f"investigate {topic}",
            "collect evidence",
            "summarize findings",
        ]


if __name__ == "__main__":
    agent = ResearchAgent()
    plan = agent.plan("model launch")
    print(plan)
