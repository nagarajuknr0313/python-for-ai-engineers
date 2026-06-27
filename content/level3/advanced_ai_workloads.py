"""Advanced Python examples for large AI workloads.

This lesson introduces batching and load estimation, two ideas useful when
preparing data or requests for parallel processing.
"""

from __future__ import annotations

from collections.abc import Sequence
from math import ceil


def batchify(items: Sequence[int], size: int) -> list[list[int]]:
    """Split a sequence into chunks for parallel processing."""
    if size <= 0:
        raise ValueError("size must be positive")

    # Slice the input into smaller groups of the requested size.
    return [list(items[index : index + size]) for index in range(0, len(items), size)]


def estimate_load(items: Sequence[int], workers: int) -> float:
    """Estimate the number of batches needed for a workload."""
    if workers <= 0:
        raise ValueError("workers must be positive")

    # Ceiling division gives the number of full batches required.
    return ceil(len(items) / workers)


if __name__ == "__main__":
    workloads = [10, 20, 30, 40]
    batches = batchify(workloads, 2)
    print(f"Batches: {batches}")
    print(f"Estimated batches for 2 workers: {estimate_load(workloads, 2)}")
