"""A minimal attention-inspired component for transformer learners.

Attention often turns a list of values into a set of scores that sum to 1.
This example shows a simple normalization step.
"""

from __future__ import annotations


def attention_scores(values: list[float]) -> list[float]:
    """Return a normalized set of attention-like scores."""
    total = sum(values)
    if total == 0:
        return [0.0 for _ in values]

    # Normalize each value so the scores add up to 1.
    return [value / total for value in values]


if __name__ == "__main__":
    scores = [2.0, 1.0, 3.0]
    print(attention_scores(scores))
