"""A simple prompt template engine for GenAI workflows."""

from __future__ import annotations


def render_prompt(task: str, tone: str) -> str:
    """Render a prompt template with user-provided values."""
    return f"Task: {task}\nTone: {tone}\nResponse: concise"


if __name__ == "__main__":
    print(render_prompt("support", "urgent"))
