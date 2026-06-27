"""Condition-based model selection for AI tasks.

This example introduces if/elif/else statements, which are used to make
simple decisions in code. In AI systems, this can decide which model is
best suited for a task.
"""

from __future__ import annotations


def choose_model(task_type: str) -> str:
    """Pick a model family based on the kind of task being handled."""
    # Different tasks benefit from different model strengths.
    if task_type == "reasoning":
        return "deep-reasoner"
    if task_type == "vision":
        return "vision-compact"
    # A fallback for general text tasks.
    return "general-chat"


if __name__ == "__main__":
    task = "vision"
    print(f"Recommended model for {task}: {choose_model(task)}")
