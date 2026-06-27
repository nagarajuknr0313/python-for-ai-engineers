# Iterators and Generators for Streaming Tokens

## Concept explanation
Iterators and generators let a program process data lazily, one piece at a time. This is useful when streaming text tokens or chunks from large documents.

## Real-world AI use case
A streaming assistant can generate output token by token instead of waiting for the full response to be built in memory.

## Execution flow
1. Define a generator that yields tokens.
2. Iterate over the tokens one at a time.
3. Process or print each token.
4. Stop when the stream has ended.

## Exercises
- Create a generator that yields chunks from a larger sentence.
- Add a pause-like delay conceptually and discuss how it might affect streaming.
- Compare a generator to a list for memory usage.

## Interview questions
- Why use a generator instead of a list?
- Where might latency-sensitive AI systems benefit from generators?
- What is the difference between an iterator and an iterable?
