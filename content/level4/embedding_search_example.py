"""A tiny similarity example for AI embeddings."""

from __future__ import annotations

from math import sqrt


def cosine_similarity(left: list[float], right: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if len(left) != len(right):
        raise ValueError("Vectors must be the same length")

    dot = sum(a * b for a, b in zip(left, right, strict=True))
    left_norm = sqrt(sum(value * value for value in left))
    right_norm = sqrt(sum(value * value for value in right))
    return dot / (left_norm * right_norm) if left_norm and right_norm else 0.0


if __name__ == "__main__":
    print(cosine_similarity([1.0, 0.0], [0.8, 0.2]))
