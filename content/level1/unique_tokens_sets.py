"""A set example for tracking unique tokens in a prompt."""

from __future__ import annotations


def collect_unique_tokens(text: str) -> set[str]:
    """Return the unique tokens from a prompt string."""
    return {token.lower() for token in text.split()}


if __name__ == "__main__":
    print(collect_unique_tokens("policy policy update update support"))
