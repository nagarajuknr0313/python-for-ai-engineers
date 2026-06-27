"""Context managers for loading AI model resources."""

from __future__ import annotations

from contextlib import contextmanager


@contextmanager
def load_model(model_name: str):
    """Simulate loading and releasing a model resource."""
    print(f"Loading {model_name}")
    try:
        yield model_name
    finally:
        print(f"Releasing {model_name}")


if __name__ == "__main__":
    with load_model("compact-ranker") as model:
        print(f"Using {model}")
