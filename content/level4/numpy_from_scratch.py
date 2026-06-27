"""A minimal NumPy-like example for AI vector math.

This example shows how vectors can be represented as lists and combined
using simple element-wise operations.
"""

from __future__ import annotations


def create_vector(values: list[float]) -> list[float]:
    """Return a vector as a list of floats."""
    return [float(value) for value in values]


def add_vectors(left: list[float], right: list[float]) -> list[float]:
    """Element-wise addition for two vectors of the same size."""
    if len(left) != len(right):
        raise ValueError("Vectors must have the same length")

    # Combine each pair of values at the same position.
    return [a + b for a, b in zip(left, right, strict=True)]


if __name__ == "__main__":
    first = create_vector([1, 2])
    second = create_vector([3, 4])
    print(add_vectors(first, second))
