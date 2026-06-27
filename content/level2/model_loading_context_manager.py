"""Context managers for loading AI model resources.

Context managers make it easier to manage setup and cleanup. Here, we
simulate loading and releasing a model resource safely around a block of
code.
"""

from __future__ import annotations

from contextlib import contextmanager


@contextmanager
def load_model(model_name: str):
    """Simulate loading and releasing a model resource."""
    print(f"Loading {model_name}")
    try:
        # The code inside the with-block can use the resource.
        yield model_name
    finally:
        # Cleanup always runs, even if an error occurs.
        print(f"Releasing {model_name}")


if __name__ == "__main__":
    with load_model("compact-ranker") as model:
        print(f"Using {model}")
