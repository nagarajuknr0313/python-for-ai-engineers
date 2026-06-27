# Variables in AI Experiment Tracking

## Concept explanation
Variables let a program store values that change as the workflow evolves. In an AI system, they can represent model names, evaluation rounds, confidence levels, or whether a feature is enabled.

## Real-world AI use case
A product team may track experiment metadata such as a model name, version number, and whether the feature is currently enabled for a controlled rollout.

## Execution flow
1. Define a model name as a string.
2. Store the evaluation round as an integer.
3. Record whether the pipeline is ready as a boolean.
4. Print the collected metadata for inspection.

## Run this concept locally
1. Open a terminal in the repository root.
2. Create and activate a virtual environment if needed.
3. Run the example with:
   ```bash
   python content/level1/ai_variables.py
   ```
4. You should see the model metadata printed in the terminal.

## Exercises
- Add a new variable for token budget.
- Change the model name and rerun the example.
- Store the current experiment state in a new dictionary.

## Interview questions
- Why are variables important in AI experiments?
- What is the difference between a string and an integer in this context?
- How would you extend this example for a multi-model benchmark?
