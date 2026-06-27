# Exception Handling for API Failures

## Concept explanation
Exceptions are errors that interrupt normal execution. Handling them allows a program to recover gracefully instead of crashing when an API or model service fails.

## Real-world AI use case
A chat application may hit rate limits or temporary network failures while calling an LLM API. Good exception handling prevents the entire app from failing.

## Execution flow
1. Attempt to process a row or call an API.
2. Catch the specific exception.
3. Log or report the failure.
4. Continue with the remaining work if possible.

## Exercises
- Create a custom exception for missing prompts.
- Add a fallback response when a call fails.
- Test the behavior with an empty input.

## Interview questions
- Why is exception handling important for AI services?
- What is the difference between catching a broad exception and a specific one?
- How would you log failures for observability?
