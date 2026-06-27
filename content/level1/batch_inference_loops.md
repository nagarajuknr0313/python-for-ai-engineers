# Loops for Batch Inference

## Concept explanation
Loops repeat a process over multiple items. In AI systems, they are used to run the same inference step over many user requests or documents.

## Real-world AI use case
A support platform might process a batch of incoming requests and generate summaries for each one in sequence.

## Execution flow
1. Create a list of items to process.
2. Loop over each item.
3. Apply a simple transformation such as a label or prefix.
4. Collect the results into a new list.

## Exercises
- Add a condition to skip empty items.
- Process a larger batch and inspect the output.
- Return both the original and processed values.

## Interview questions
- Why are loops valuable in batch inference?
- How would you adapt this pattern for API calls?
- What is the difference between a loop and a list comprehension here?
