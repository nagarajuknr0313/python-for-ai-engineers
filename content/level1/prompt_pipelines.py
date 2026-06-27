"""A prompt pipeline example for AI task routing."""

from __future__ import annotations


def build_prompt_pipeline(task: str, context: str) -> str:
    """Create a multi-step prompt pipeline string."""
    return f"Task: {task}\nContext: {context}\nAction: draft a concise reply"


if __name__ == "__main__":
    print(build_prompt_pipeline("summarize incident", "customer reported a login issue"))
