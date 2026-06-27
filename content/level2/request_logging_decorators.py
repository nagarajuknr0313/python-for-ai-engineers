"""Decorators for logging AI requests."""

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
    return f"processed:{prompt}"


if __name__ == "__main__":
    submit_prompt("draft a triage summary")
