"""A simple multiprocessing-style example for embedding generation."""

from __future__ import annotations

from multiprocessing import Pool


def embed_text(text: str) -> tuple[str, int]:
    """Return a simple embedding signature for text."""
    return text, len(text.split())


if __name__ == "__main__":
    with Pool(processes=2) as pool:
        results = pool.map(embed_text, ["support ticket", "refund request"])
    print(results)
