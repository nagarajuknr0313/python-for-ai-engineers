"""Looping through batch inference requests."""

from __future__ import annotations


def run_batch(items: list[str]) -> list[str]:
    """Simulate a simple batch inference pass."""
    results: list[str] = []
    for item in items:
        results.append(f"processed:{item}")
    return results


if __name__ == "__main__":
    print(run_batch(["invoice", "refund", "policy"])))
