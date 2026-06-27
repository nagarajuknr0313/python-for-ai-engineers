"""Basic vector operations for AI learners."""

from __future__ import annotations


def dot_product(left: list[float], right: list[float]) -> float:
    """Compute the dot product of two vectors."""
    if len(left) != len(right):
        raise ValueError("Vectors must have the same length")
    return sum(a * b for a, b in zip(left, right, strict=True))


if __name__ == "__main__":
    print(dot_product([1.0, 2.0], [3.0, 4.0]))
