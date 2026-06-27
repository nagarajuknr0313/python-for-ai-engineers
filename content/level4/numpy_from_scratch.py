"""A minimal NumPy-like example for AI vector math."""

from __future__ import annotations


def create_vector(values: list[float]) -> list[float]:
    """Return a vector as a list of floats."""
    return [float(value) for value in values]


def add_vectors(left: list[float], right: list[float]) -> list[float]:
    """Element-wise addition."""
    if len(left) != len(right):
        raise ValueError("Vectors must have the same length")
    return [a + b for a, b in zip(left, right, strict=True)]


if __name__ == "__main__":
    print(add_vectors(create_vector([1, 2]), create_vector([3, 4])))
