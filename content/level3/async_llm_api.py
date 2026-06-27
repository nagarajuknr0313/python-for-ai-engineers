"""A minimal asynchronous example for LLM-style API calls.

Async code helps keep programs responsive when waiting on external work,
such as API calls or I/O-bound operations.
"""

from __future__ import annotations

import asyncio


async def fetch_summary(prompt: str) -> str:
    """Simulate a non-blocking LLM response."""
    # A short delay models waiting for a remote service.
    await asyncio.sleep(0.01)
    return f"summary:{prompt}"


async def main() -> None:
    result = await fetch_summary("summarize the incident")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
