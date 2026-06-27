# JSON for LLM Responses

## Concept explanation
JSON is a lightweight format for structured data. It is widely used to store model outputs, configuration objects, and intermediate results in AI systems.

## Real-world AI use case
An application may persist a model response as JSON so a downstream service can interpret fields such as answer, citations, and confidence.

## Execution flow
1. Build a response payload as a Python dictionary.
2. Convert it to JSON text.
3. Write the JSON to a file.
4. Load it back and inspect the structure.

## Exercises
- Add a field for citations.
- Make the response include a confidence score.
- Parse the JSON and print one field.

## Interview questions
- Why is JSON well suited to LLM outputs?
- What are common fields in an AI response payload?
- How does JSON differ from CSV?
