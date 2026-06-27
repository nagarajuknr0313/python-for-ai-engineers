"""A simple embedding sketch for product feedback analysis."""

from __future__ import annotations


def build_embedding(idea: str) -> list[float]:
    """Map a short idea into a small numeric vector."""
    tokens = idea.lower().split()
    return [len(tokens), sum(ord(ch) for ch in idea) / 1000.0, 1.0]


if __name__ == "__main__":
    print(build_embedding("fast multilingual support"))
