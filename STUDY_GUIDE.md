# Study Guide

This repository is organized as a six-level curriculum for learning Python through AI engineering scenarios.

## How to Use This Repository
1. Start with Level 1 and work through each topic in order.
2. Open the README in each level for the learning path and topic list.
3. Read the lesson markdown file for the concept explanation and exercises.
4. Run the matching Python example file.
5. Use the tests as a quick validation step.

## Curriculum Map
- Level 1: Python Fundamentals
  - Prerequisite: no prior Python experience needed.
- Level 2: Intermediate Python
  - Prerequisite: complete Level 1.
- Level 3: Advanced Python
  - Prerequisite: complete Level 2.
- Level 4: Python for AI
  - Prerequisite: complete Level 3.
- Level 5: Python for LLMs and GenAI
  - Prerequisite: complete Level 4.
- Level 6: Python for AI Agents
  - Prerequisite: complete Level 5.

## Suggested Progression
- Week 1: Levels 1 and 2
- Week 2: Levels 3 and 4
- Week 3: Levels 5 and 6

## Learning Flow
Each level is designed to be a distinct checkpoint. Do not jump to the next level until you can explain the core ideas from the current one and run its example code successfully.

## Local Run Guide
Use the following steps to run the project on your machine:

```powershell
cd d:\AI Work\python-for-ai-engineers
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python content\level1\variables_and_types.py
python -m pytest -q
```

## Learning Outcomes
By the end of the repository, learners should be able to:
- Write Python for AI workflows
- Work with vectors, embeddings, and prompt templates
- Build simple retrieval and agent systems
- Structure code in a production-like way
