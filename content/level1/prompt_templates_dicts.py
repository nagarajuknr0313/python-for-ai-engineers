"""A dictionary-based prompt template system for AI tasks.

Dictionaries are a great way to group related values under clear names.
Here, we store the task, tone, and rendered prompt in one structure.
"""

from __future__ import annotations


def build_prompt(task: str, tone: str) -> dict[str, str]:
    """Create a prompt payload for a model request."""
    return {
        # Keys give meaning to the values stored in the dictionary.
        "task": task,
        "tone": tone,
        "prompt": f"Write a {tone} response for the task: {task}",
    }


if __name__ == "__main__":
    prompt_payload = build_prompt("summarize support feedback", "calm")
    print(prompt_payload)
