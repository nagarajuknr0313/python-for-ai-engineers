# Tuples for Model Configurations

## Concept explanation
A tuple is an immutable sequence. It is useful when a piece of data should stay fixed, such as a small model configuration that should not be accidentally modified.

## Real-world AI use case
A deployment pipeline might package model name, version, and temperature into a tuple so configuration remains stable during rollout.

## Execution flow
1. Create a tuple containing a model name, version, and temperature.
2. Print the tuple values.
3. Use the tuple as a compact configuration record.
4. Pass it into a function if needed.

## Exercises
- Add a new field such as max_tokens.
- Try to modify one element and observe the error.
- Compare tuple behavior with a list.

## Interview questions
- Why would you choose a tuple for configuration data?
- What does immutability mean in this context?
- How is a tuple different from a list in an AI pipeline?
