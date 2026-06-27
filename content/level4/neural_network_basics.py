"""A tiny neural network-inspired example for AI learners.

This simple function mirrors the core computation of a single neuron: a
weighted input plus a bias.
"""

from __future__ import annotations


def predict(input_value: float, weight: float, bias: float) -> float:
    """Return a simple linear prediction."""
    return input_value * weight + bias


if __name__ == "__main__":
    value = 2.0
    weight = 0.5
    bias = 1.0
    print(f"Prediction: {predict(value, weight, bias)}")
