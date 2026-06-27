"""A function-based prompt pipeline for AI answer drafting.

This example shows how small helper functions can make code easier to read
and reuse. Each function has one job: normalize the context and build the
prompt.
"""

from __future__ import annotations


def normalize_context(context: str) -> str:
    """Trim whitespace and lowercase the context text."""
    return context.strip().lower()


def build_prompt(context: str, task: str) -> str:
    """Create a prompt string from context and task."""
    cleaned_context = normalize_context(context)
    return f"Task: {task}\nContext: {cleaned_context}"


if __name__ == "__main__":
    context = "  Support policy update  "
    task = "Summarize for a new agent"
    print(build_prompt(context, task))
