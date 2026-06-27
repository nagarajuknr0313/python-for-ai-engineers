# Tool Calling and Function Calling

## Concept explanation
Tool calling lets an agent use external capabilities such as searching, fetching data, or running code. Function calling is a structured way to ask the model to invoke a known function with arguments.

## Real-world AI use case
An agent may call a calendar tool to schedule a follow-up meeting or a search tool to retrieve up-to-date product information.

## Execution flow
1. Define a tool or function.
2. Describe the tool to the agent.
3. Pass the task to the model or planner.
4. Execute the tool and return the result.

## Exercises
- Add a second tool such as a calculator.
- Write a small wrapper that routes tasks to tools.
- Describe how the tool output influences the final answer.

## Interview questions
- Why are tools important in agent systems?
- How does function calling differ from plain prompting?
- What risks come with granting agents tool access?
