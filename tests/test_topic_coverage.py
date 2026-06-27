import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(module_name: str, relative_path: str):
    module_path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_type_hints_pipeline_builds_payload() -> None:
    module = load_module("type_hints_pipeline", "content/level2/type_hints_pipeline.py")
    payload = module.build_typed_request("summarize", "support")
    assert payload["task"] == "summarize"
    assert payload["context"] == "support"


def test_multithreading_inference_batches_requests() -> None:
    module = load_module("multithreading_inference", "content/level3/multithreading_inference.py")
    result = module.run_batch_inference(["a", "b"])
    assert result == ["inferred:a", "inferred:b"]


def test_vector_operations_compute_dot_product() -> None:
    module = load_module("vector_operations", "content/level4/vector_operations.py")
    assert module.dot_product([1.0, 2.0], [3.0, 4.0]) == 11.0


def test_prompt_template_engine_renders_text() -> None:
    module = load_module("prompt_template_engine", "content/level5/prompt_template_engine.py")
    rendered = module.render_prompt("support", "urgent")
    assert "support" in rendered and "urgent" in rendered


def test_research_agent_creates_plan() -> None:
    module = load_module("research_agent", "content/level6/research_agent.py")
    agent = module.ResearchAgent()
    assert agent.plan("launch")
