"""Looping through batch inference requests.

This example shows how for loops can process many inputs in a predictable
way. In AI systems, loops are useful for running the same operation over a
batch of prompts or documents.
"""

from __future__ import annotations


def run_batch(items: list[str]) -> list[str]:
    """Simulate processing a collection of prompts in a batch."""
    results: list[str] = []
    # Each item is handled one by one in the loop.
    for item in items:
        results.append(f"processed:{item}")
    return results


if __name__ == "__main__":
    prompts = ["invoice", "refund", "policy"]
    print(run_batch(prompts))
