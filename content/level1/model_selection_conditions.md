# Conditions for Model Selection

## Concept explanation
Conditionals allow a program to choose different paths based on input. In AI systems, they are often used to select a model or strategy based on task category or complexity.

## Real-world AI use case
A routing service can choose a reasoning model for difficult tasks and a lighter model for simpler requests, reducing cost and latency.

## Execution flow
1. Receive a task type such as reasoning or vision.
2. Check which condition matches.
3. Return the appropriate model name.
4. Print the selected model.

## Exercises
- Add a new task type such as summarization.
- Create a fallback model for unsupported requests.
- Extend the function to log the decision.

## Interview questions
- How do conditionals help with model routing?
- Why might you want a fallback model?
- How can this reduce cost in production?
