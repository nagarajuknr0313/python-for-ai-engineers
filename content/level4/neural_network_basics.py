"""A tiny neural network-inspired example for AI learners."""

from __future__ import annotations


def predict(input_value: float, weight: float, bias: float) -> float:
    """Return a simple linear prediction."""
    return input_value * weight + bias


if __name__ == "__main__":
    print(predict(2.0, 0.5, 1.0))
