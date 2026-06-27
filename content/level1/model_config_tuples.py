"""A tuple-based example for model configuration settings."""

from __future__ import annotations


def build_model_config() -> tuple[str, int, float]:
    """Return a compact model configuration tuple."""
    return ("vision-compact", 4, 0.7)


if __name__ == "__main__":
    print(build_model_config())
