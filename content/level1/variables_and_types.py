"""Original Python lesson using AI experiment metadata.

This module demonstrates variables and basic data types in a fictional
AI model evaluation workflow.
"""

from __future__ import annotations

model_name = "nebula-vision"
model_version = 3
is_multimodal = True
embedding_dimension = 768

prompt_token_budget = 4096
prompt_template = "Summarize the incident report for a support copilot."

vector_snapshot = [0.12, -0.31, 0.88, 0.55]

print(f"Model: {model_name} v{model_version}")
print(f"Multimodal ready: {is_multimodal}")
print(f"Embedding dimension: {embedding_dimension}")
print(f"Prompt budget: {prompt_token_budget}")
print(f"Prompt template: {prompt_template}")
print(f"Vector snapshot: {vector_snapshot}")
