import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "content" / "level3" / "advanced_ai_workloads.py"

spec = importlib.util.spec_from_file_location("advanced_ai_workloads", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_batchify_groups_items() -> None:
    assert module.batchify([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_estimate_load_returns_positive_value() -> None:
    estimate = module.estimate_load([1, 2, 3, 4, 5], 2)
    assert estimate > 0
