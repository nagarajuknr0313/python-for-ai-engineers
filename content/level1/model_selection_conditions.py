"""Condition-based model selection for AI tasks."""

from __future__ import annotations


def choose_model(task_type: str) -> str:
    """Select a model family based on task complexity."""
    if task_type == "reasoning":
        return "deep-reasoner"
    if task_type == "vision":
        return "vision-compact"
    return "general-chat"


if __name__ == "__main__":
    print(choose_model("vision"))
