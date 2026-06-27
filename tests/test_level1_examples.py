from pathlib import Path

import importlib.util


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "content" / "level1" / "variables_and_types.py"


spec = importlib.util.spec_from_file_location("variables_and_types", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_basic_variables_exist() -> None:
    assert module.model_name == "nebula-vision"
    assert module.model_version == 3
    assert module.is_multimodal is True


def test_vector_snapshot_is_list() -> None:
    assert isinstance(module.vector_snapshot, list)
    assert len(module.vector_snapshot) == 4
