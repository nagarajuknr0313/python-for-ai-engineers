# Sets for Unique Tokens

## Concept explanation
A set stores unique values and removes duplicates automatically. This is useful when tracking vocabulary tokens or filtering repeated terms from a prompt.

## Real-world AI use case
A moderation pipeline can inspect incoming prompts and detect which unique tokens appear most often without counting duplicates.

## Execution flow
1. Split the text into tokens.
2. Convert them into a set.
3. Print the resulting unique tokens.
4. Use the set as a lightweight vocabulary summary.

## Exercises
- Add a repeated token and verify it is not duplicated.
- Create a set for a second prompt and compare them.
- Explain how a set differs from a list here.

## Interview questions
- Why would you choose a set over a list for token analysis?
- What happens if you need to preserve order?
- How could this help with prompt filtering?
