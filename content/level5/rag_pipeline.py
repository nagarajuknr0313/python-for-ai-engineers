"""A compact retrieval-augmented generation example for support copilots."""

from __future__ import annotations


def chunk_text(text: str, size: int) -> list[str]:
    """Split a document into chunks of a given size."""
    words = text.split()
    if size <= 0:
        raise ValueError("size must be positive")
    return [" ".join(words[index : index + size]) for index in range(0, len(words), size)]


def retrieve_relevant_chunks(query: str, chunks: list[str]) -> list[str]:
    """Return chunks that contain the query string."""
    return [chunk for chunk in chunks if query.lower() in chunk.lower()]


if __name__ == "__main__":
    document = "policy update includes new support steps for escalation"
    chunks = chunk_text(document, 3)
    print(chunks)
    print(retrieve_relevant_chunks("support", chunks))
