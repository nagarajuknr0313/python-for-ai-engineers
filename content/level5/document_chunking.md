# Document Chunking

## Concept explanation
Chunking divides a large document into smaller pieces so retrieval and context window usage remain efficient.

## Real-world AI use case
A knowledge base assistant can chunk policy documents and retrieve only the most relevant sections.

## Execution flow
1. Split a large document into chunks.
2. Store the chunks with metadata.
3. Retrieve chunks for a query.
4. Pass the selected chunks to the model.

## Exercises
- Change the chunk size and compare results.
- Add metadata for each chunk.
- Build a small retrieval function for the chunks.

## Interview questions
- Why is chunking needed for long documents?
- What happens if chunks are too large?
- How does overlap help retrieval?
