import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "content" / "level6" / "agent_workflow.py"

spec = importlib.util.spec_from_file_location("agent_workflow", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_planner_agent_returns_steps() -> None:
    planner = module.PlannerAgent()
    plan = planner.plan("research the new model launch")
    assert isinstance(plan, list)
    assert plan
