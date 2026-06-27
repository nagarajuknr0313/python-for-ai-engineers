"""A simple multithreading example for inference workloads.

Threads can help process several lightweight tasks at the same time. In this
example, we simulate inference for a short batch of items.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor


def infer_item(item: str) -> str:
    """Simulate an inference call for a single request."""
    return f"inferred:{item}"


def run_batch_inference(items: list[str]) -> list[str]:
    """Run inference for a batch of items using threads."""
    with ThreadPoolExecutor(max_workers=2) as executor:
        # map applies the function to each item concurrently.
        return list(executor.map(infer_item, items))


if __name__ == "__main__":
    requests = ["a", "b", "c"]
    print(run_batch_inference(requests))
