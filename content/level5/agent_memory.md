# Agent Memory

## Concept explanation
Agent memory stores context that helps a system stay coherent across multiple steps or turns.

## Real-world AI use case
A planning assistant can remember earlier user constraints so it does not forget them later in the workflow.

## Execution flow
1. Capture important state from the task.
2. Store the state in memory.
3. Retrieve the memory in later steps.
4. Use it to shape the final response.

## Exercises
- Add a constraint to the memory and use it in a later step.
- Create a memory reset function.
- Discuss how memory size impacts performance.

## Interview questions
- Why is memory important for agents?
- What is the difference between memory and context?
- How can stale memory hurt an agent?
