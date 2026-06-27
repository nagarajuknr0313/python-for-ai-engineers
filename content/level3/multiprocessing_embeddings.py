"""A simple multiprocessing-style example for embedding generation.

Processes are useful when work is CPU-heavy. This example shows a basic
parallel map over a small list of texts.
"""

from __future__ import annotations

from multiprocessing import Pool


def embed_text(text: str) -> tuple[str, int]:
    """Return a simple embedding signature for text."""
    # A lightweight stand-in for embedding size based on word count.
    return text, len(text.split())


if __name__ == "__main__":
    with Pool(processes=2) as pool:
        results = pool.map(embed_text, ["support ticket", "refund request"])
    print(results)
