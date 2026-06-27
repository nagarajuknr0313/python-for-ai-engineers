"""A simple multithreading example for inference workloads."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor


def infer_item(item: str) -> str:
    """Simulate an inference call for a single request."""
    return f"inferred:{item}"


def run_batch_inference(items: list[str]) -> list[str]:
    """Run inference for a batch of items using threads."""
    with ThreadPoolExecutor(max_workers=2) as executor:
        return list(executor.map(infer_item, items))


if __name__ == "__main__":
    print(run_batch_inference(["a", "b"]))
