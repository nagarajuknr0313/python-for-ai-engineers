import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "content" / "level5" / "rag_pipeline.py"

spec = importlib.util.spec_from_file_location("rag_pipeline", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_chunk_text_creates_expected_segments() -> None:
    chunks = module.chunk_text("one two three four", 2)
    assert chunks == ["one two", "three four"]


def test_retrieve_relevant_chunks_returns_matches() -> None:
    chunks = ["alpha beta", "gamma delta"]
    matches = module.retrieve_relevant_chunks("beta", chunks)
    assert matches == ["alpha beta"]
