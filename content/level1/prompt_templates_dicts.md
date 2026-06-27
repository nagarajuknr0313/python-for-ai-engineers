# Dictionaries for Prompt Templates

## Concept explanation
Dictionaries store values as key-value pairs. In prompt engineering, they are ideal for bundling task instructions, tones, and generated prompt text in one structure.

## Real-world AI use case
A content generation assistant can use dictionaries to keep the task, tone, and prompt body together before sending them to a language model.

## Execution flow
1. Create a dictionary with keys such as task and tone.
2. Build a prompt string from those values.
3. Print the final prompt payload.
4. Reuse the structure for other prompts.

## Run this concept locally
1. Open a terminal in the repository root.
2. Run the example with:
   ```bash
   python content/level1/prompt_templates_dicts.py
   ```
3. The script will print the prompt payload as a dictionary.

## Exercises
- Add a new key for audience.
- Build a second prompt with a different tone.
- Refactor the function to return a more complete payload.

## Interview questions
- Why are dictionaries useful for prompt templates?
- What other metadata might you store with a prompt?
- How would you handle multiple prompt variants?
