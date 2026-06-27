"""A simple research agent example."""

from __future__ import annotations


class ResearchAgent:
    """Create a basic research plan for a topic."""

    def plan(self, topic: str) -> list[str]:
        """Return a short research plan."""
        return [f"investigate {topic}", "collect evidence", "summarize findings"]


if __name__ == "__main__":
    agent = ResearchAgent()
    print(agent.plan("model launch"))
