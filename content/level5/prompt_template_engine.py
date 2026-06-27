"""A simple prompt template engine for GenAI workflows.

Prompt templates help standardize how requests are assembled before sending
them to a language model.
"""

from __future__ import annotations


def render_prompt(task: str, tone: str) -> str:
    """Render a prompt template with user-provided values."""
    return f"Task: {task}\nTone: {tone}\nResponse: concise"


if __name__ == "__main__":
    prompt = render_prompt("support", "urgent")
    print(prompt)
