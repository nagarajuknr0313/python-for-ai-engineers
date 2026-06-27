"""Simple design patterns commonly used in AI systems.

The strategy pattern lets us swap behaviors without changing the rest of the
code. Here, the builder uses a prompt strategy to construct different outputs.
"""

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
