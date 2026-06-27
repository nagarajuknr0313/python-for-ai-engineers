"""A tiny gradient descent example for understanding optimization."""

from __future__ import annotations


def optimize(weight: float, learning_rate: float, gradient: float) -> float:
    """Update a weight using a simple gradient step."""
    return weight - learning_rate * gradient


if __name__ == "__main__":
    print(optimize(1.0, 0.1, 0.2))
