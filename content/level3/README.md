# Level 3: Advanced Python

This level focuses on Python patterns that matter when AI systems must scale, handle concurrency, and stay observable.

## Topics and Code Files
1. Multithreading for parallel inference: [advanced_ai_workloads.py](advanced_ai_workloads.py)
2. Multiprocessing for embeddings generation: [multiprocessing_embeddings.py](multiprocessing_embeddings.py)
3. Async programming for LLM APIs: [async_llm_api.py](async_llm_api.py)
4. Memory optimization for large datasets: [memory_and_profiling.md](memory_and_profiling.md)
5. Profiling AI workloads: [memory_and_profiling.md](memory_and_profiling.md)
6. Design patterns used in AI systems: [design_patterns.py](design_patterns.py)

## Unique Example
A batch inference controller that distributes model scoring work across a queue of incoming requests while tracking runtime and memory pressure.

## Lesson Pages
- [Parallel Inference and Workload Batching](parallel_inference.md)
- [Memory Optimization and Profiling](memory_and_profiling.md)
