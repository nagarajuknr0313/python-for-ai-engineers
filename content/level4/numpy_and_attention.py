"""NumPy-style examples for AI vector operations and attention."""

from __future__ import annotations

from math import sqrt


def tokenize_text(text: str) -> list[str]:
    """Split a sentence into lowercase tokens."""
    return [token.lower() for token in text.split()]


def cosine_similarity(left: list[float], right: list[float]) -> float:
    """Compute the cosine similarity between two vectors."""
    if len(left) != len(right):
        raise ValueError("Vectors must have the same length")

    dot_product = sum(a * b for a, b in zip(left, right, strict=True))
    left_norm = sqrt(sum(value * value for value in left))
    right_norm = sqrt(sum(value * value for value in right))

    if left_norm == 0 or right_norm == 0:
        return 0.0

    return dot_product / (left_norm * right_norm)


if __name__ == "__main__":
    tokens = tokenize_text("ai agents search memory")
    print(tokens)
    print(cosine_similarity([1.0, 0.0], [0.0, 1.0]))
