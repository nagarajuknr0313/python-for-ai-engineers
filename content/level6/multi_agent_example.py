"""A small multi-agent workflow example."""

from __future__ import annotations


class ResearchAgent:
    """Collect evidence for a task."""

    def gather(self, topic: str) -> list[str]:
        return [f"finding for {topic}"]


class WritingAgent:
    """Turn findings into a short report."""

    def draft(self, findings: list[str]) -> str:
        return " | ".join(findings)


if __name__ == "__main__":
    research = ResearchAgent()
    writing = WritingAgent()
    findings = research.gather("new model launch")
    print(writing.draft(findings))
