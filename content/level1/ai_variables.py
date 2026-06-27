"""Original variable example for AI experiment tracking."""

from __future__ import annotations


def track_experiment() -> dict[str, object]:
    """Store experiment metadata for a model run."""
    model_name = "aurora-lite"
    evaluation_round = 4
    is_ready = True
    return {"model_name": model_name, "evaluation_round": evaluation_round, "is_ready": is_ready}


if __name__ == "__main__":
    print(track_experiment())
