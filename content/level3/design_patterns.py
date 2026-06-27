"""Simple design patterns commonly used in AI systems."""

from __future__ import annotations


class PromptStrategy:
    """A simple strategy pattern for prompt styles."""

    def build(self, task: str) -> str:
        return f"strategy:{task}"


class PromptBuilder:
    """Wrap a strategy and delegate prompt creation."""

    def __init__(self, strategy: PromptStrategy) -> None:
        self.strategy = strategy

    def build(self, task: str) -> str:
        return self.strategy.build(task)


if __name__ == "__main__":
    builder = PromptBuilder(PromptStrategy())
    print(builder.build("triage a support request"))
