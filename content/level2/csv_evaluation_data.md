# CSV for Evaluation Data

## Concept explanation
CSV stores tabular data as plain text with rows and columns. It is a practical format for evaluation datasets because many tools and spreadsheets can read it.

## Real-world AI use case
A quality team may keep prompts and expected labels in a CSV file so an evaluation script can score model responses automatically.

## Execution flow
1. Open the CSV file.
2. Read each row as a dictionary.
3. Inspect the prompt and expected label.
4. Use the row to prepare an evaluation case.

## Exercises
- Add a new evaluation row.
- Filter rows by expected label.
- Save the filtered rows to a new file.

## Interview questions
- Why is CSV commonly used for evaluation datasets?
- How does a CSV row differ from a JSON object?
- What are the advantages of structured data formats?
