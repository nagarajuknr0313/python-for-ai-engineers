import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "content" / "level4" / "numpy_and_attention.py"

spec = importlib.util.spec_from_file_location("numpy_and_attention", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_tokenize_text_splits_words() -> None:
    tokens = module.tokenize_text("alpha beta gamma")
    assert tokens == ["alpha", "beta", "gamma"]


def test_cosine_similarity_is_bounded() -> None:
    score = module.cosine_similarity([1.0, 0.0], [0.0, 1.0])
    assert score == 0.0
