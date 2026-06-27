"""A minimal attention-inspired component for transformer learners."""

from __future__ import annotations


def attention_scores(values: list[float]) -> list[float]:
    """Return a normalized set of attention-like scores."""
    total = sum(values)
    if total == 0:
        return [0.0 for _ in values]
    return [value / total for value in values]


if __name__ == "__main__":
    print(attention_scores([2.0, 1.0, 3.0]))
