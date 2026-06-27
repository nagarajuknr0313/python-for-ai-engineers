"""A function-based prompt pipeline for AI answer drafting."""

from __future__ import annotations


def normalize_context(context: str) -> str:
    """Trim and lowercase context text."""
    return context.strip().lower()


def build_prompt(context: str, task: str) -> str:
    """Create a prompt string from context and task."""
    cleaned_context = normalize_context(context)
    return f"Task: {task}\nContext: {cleaned_context}"


if __name__ == "__main__":
    print(build_prompt("  Support policy update  ", "Summarize for a new agent"))
