"""Advanced Python examples for large AI workloads."""

from __future__ import annotations

from collections.abc import Sequence
from math import ceil


def batchify(items: Sequence[int], size: int) -> list[list[int]]:
    """Split a sequence into chunks for parallel processing."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [list(items[index : index + size]) for index in range(0, len(items), size)]


def estimate_load(items: Sequence[int], workers: int) -> float:
    """Estimate the number of batches needed for a workload."""
    if workers <= 0:
        raise ValueError("workers must be positive")
    return ceil(len(items) / workers)


if __name__ == "__main__":
    batches = batchify([10, 20, 30, 40], 2)
    print(batches)
    print(estimate_load([10, 20, 30, 40, 50], 2))
