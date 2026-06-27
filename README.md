# Python for AI Engineers

![Python Tests](https://github.com/OWNER/REPOSITORY/actions/workflows/python-tests.yml/badge.svg)

A completely original, project-based course repository that teaches Python through AI, LLM, RAG, embeddings, agents, and product development use cases.

## Repository Goals
- Teach Python from beginner to advanced through AI-centric examples
- Keep every example original and tailored to modern AI systems
- Provide production-like code, tests, and structured exercises

## Learning Levels
1. Level 1: Python Fundamentals
   - Start here if you are new to Python.
   - Focus: variables, collections, conditions, loops, functions, and classes.
2. Level 2: Intermediate Python
   - Continue after Level 1.
   - Focus: files, JSON, CSV, exceptions, iterators, generators, decorators, context managers, and type hints.
3. Level 3: Advanced Python
   - Move here once you are comfortable with structured code.
   - Focus: concurrency, async programming, memory awareness, profiling, and design patterns.
4. Level 4: Python for AI
   - Begin after Level 3.
   - Focus: NumPy-style vectors, similarity, tokenization, preprocessing, and basic neural network ideas.
5. Level 5: Python for LLMs and GenAI
   - Continue after Level 4.
   - Focus: prompt design, memory, RAG, embeddings, search, tool use, and function calling.
6. Level 6: Python for AI Agents
   - Finish here once you understand the earlier foundations.
   - Focus: research agents, coding agents, planners, memory, reflection, and multi-agent workflows.

## Repository Structure
```text
python-for-ai-engineers/
├── README.md
├── requirements.txt
├── pyproject.toml
├── src/
│   └── python_for_ai_engineers/
│       └── __init__.py
├── content/
│   ├── level1/
│   ├── level2/
│   ├── level3/
│   ├── level4/
│   ├── level5/
│   └── level6/
├── tests/
└── notebooks/
```

## Getting Started
1. Create a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Explore the level modules in the content folder.
4. Run the tests:
   ```powershell
   python -m pytest -q
   ```

## Learning Path
- Start with [STUDY_GUIDE.md](STUDY_GUIDE.md)
- Review the topic coverage checklist in [TOPIC_COVERAGE.md](TOPIC_COVERAGE.md)
- Explore [content/level1/README.md](content/level1/README.md)
- Continue through the remaining levels in the content folder

## Notes
All examples are designed to be original and domain-specific to AI engineering workflows.
