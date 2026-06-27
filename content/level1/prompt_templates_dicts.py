"""A dictionary-based prompt template system for AI tasks."""

from __future__ import annotations


def build_prompt(task: str, tone: str) -> dict[str, str]:
    """Create a prompt payload for a model request."""
    return {
        "task": task,
        "tone": tone,
        "prompt": f"Write a {tone} response for the task: {task}",
    }


if __name__ == "__main__":
    print(build_prompt("summarize support feedback", "calm"))
