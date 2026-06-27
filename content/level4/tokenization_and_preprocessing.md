# Tokenization and Text Preprocessing

## Concept explanation
Tokenization breaks text into smaller units, while preprocessing cleans and normalizes the text before it is used in a model. These steps help prepare data for embeddings, classification, and generation.

## Real-world AI use case
An AI support system might preprocess customer messages by lowercasing and stripping punctuation before turning them into tokens for analysis.

## Execution flow
1. Receive an input sentence.
2. Normalize the text.
3. Split it into tokens.
4. Use the tokens as input to downstream logic.

## Exercises
- Add punctuation cleanup to the example.
- Create a token list for a longer message.
- Compare the effect of lowercasing.

## Interview questions
- Why is preprocessing important before tokenization?
- What is the difference between a token and a word?
- How could poor preprocessing harm model performance?
