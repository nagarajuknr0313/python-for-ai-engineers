# Embeddings and Vectors

## Concept explanation
Embeddings transform symbols or ideas into numeric vectors so a computer can compare them mathematically. The vector values are not random; they capture relationships that support similarity search and retrieval.

## Real-world AI use case
A product support system might convert customer feedback into vectors to group similar complaints and detect repeated themes.

## Execution flow
1. Write a short phrase such as a support issue.
2. Convert the phrase into a lightweight numeric vector.
3. Print the vector to inspect its structure.
4. Use the vector as a starting point for similarity analysis.

## Run this concept locally
1. Open a terminal in the repository root.
2. Run the example with:
   ```bash
   python content/level1/embeddings_and_vectors.py
   ```
3. The script will print a small vector-like output for the provided idea.

## Exercises
- Create a vector for a second idea and compare its shape.
- Add a third numeric feature to the embedding.
- Explain why the values might differ for similar ideas.

## Interview questions
- What is the purpose of an embedding?
- Why might two semantically similar ideas produce different vectors?
- How does this differ from plain text storage?
