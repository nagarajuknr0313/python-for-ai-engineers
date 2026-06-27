from pathlib import Path

import importlib.util


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "content" / "level2" / "ai_pipeline.py"


spec = importlib.util.spec_from_file_location("ai_pipeline", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_process_case_requires_prompt() -> None:
    try:
        module.process_case({"prompt": ""})
    except module.ApiFailure:
        assert True
    else:
        assert False, "Expected ApiFailure for a missing prompt"


def test_stream_tokens_yields_words() -> None:
    tokens = list(module.stream_tokens("alpha beta"))
    assert tokens == ["alpha", "beta"]
