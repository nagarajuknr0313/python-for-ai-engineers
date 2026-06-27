"""Generators for chunk processing in AI document workflows."""

from __future__ import annotations


def yield_chunks(text: str, size: int) -> list[str]:
    """Yield document chunks of a given size."""
    if size <= 0:
        raise ValueError("size must be positive")
    words = text.split()
    return [" ".join(words[index:index + size]) for index in range(0, len(words), size)]


if __name__ == "__main__":
    print(yield_chunks("policy update support escalation routing", 2))
