"""A simple workload batching example for AI inference pipelines."""

from __future__ import annotations


def batch_requests(items: list[str], batch_size: int) -> list[list[str]]:
    """Split requests into batches for parallel processing."""
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    return [items[index : index + batch_size] for index in range(0, len(items), batch_size)]


if __name__ == "__main__":
    print(batch_requests(["a", "b", "c", "d"], 2))
