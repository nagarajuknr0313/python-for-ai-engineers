"""Decorators for logging AI requests.

Decorators wrap a function with extra behavior. In this example, the
wrapper logs the input and output of a prompt submission function.
"""

from __future__ import annotations


def log_request(func):
    """Wrap a function and log its input and output."""

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


@log_request
def submit_prompt(prompt: str) -> str:
    """Simulate processing a prompt."""
    return f"processed:{prompt}"


if __name__ == "__main__":
    submit_prompt("draft a triage summary")
