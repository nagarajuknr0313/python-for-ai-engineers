"""A tiny gradient descent example for understanding optimization.

Gradient descent updates a parameter in the direction that reduces error.
This example uses a very small step to illustrate the idea.
"""

from __future__ import annotations


def optimize(weight: float, learning_rate: float, gradient: float) -> float:
    """Update a weight using a simple gradient step."""
    return weight - learning_rate * gradient


if __name__ == "__main__":
    current_weight = 1.0
    learning_rate = 0.1
    gradient = 0.2
    print(f"Updated weight: {optimize(current_weight, learning_rate, gradient)}")
