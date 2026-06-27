"""Variables and basic data types in an AI workflow.

This example shows how Python stores simple values such as strings,
integers, booleans, and lists. These concepts are foundational when
working with model metadata, prompts, and embeddings.
"""

from __future__ import annotations

# Strings describe models and prompts.
model_name = "nebula-vision"
model_version = 3  # Integers are useful for version numbers.
is_multimodal = True  # Booleans represent yes/no states.
embedding_dimension = 768  # A common size for embeddings.

# A larger integer can represent a token budget.
prompt_token_budget = 4096
# A string stores the prompt text that will be sent to a model.
prompt_template = "Summarize the incident report for a support copilot."

# A list stores a small vector snapshot, which is useful in AI work.
vector_snapshot = [0.12, -0.31, 0.88, 0.55]

# Printing values helps us inspect the data in a readable way.
print(f"Model: {model_name} v{model_version}")
print(f"Multimodal ready: {is_multimodal}")
print(f"Embedding dimension: {embedding_dimension}")
print(f"Prompt budget: {prompt_token_budget}")
print(f"Prompt template: {prompt_template}")
print(f"Vector snapshot: {vector_snapshot}")
