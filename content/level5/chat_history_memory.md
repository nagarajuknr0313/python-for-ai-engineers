# Chat History Memory

## Concept explanation
Memory keeps a record of earlier turns so the system can respond with context and continuity.

## Real-world AI use case
A product concierge can remember the user’s previous questions and avoid repeating itself.

## Execution flow
1. Store each turn in a history list.
2. Retrieve the relevant earlier messages.
3. Include them in the next prompt.
4. Continue the conversation.

## Exercises
- Add a follow-up turn and inspect the memory.
- Limit the memory size and discuss the trade-off.
- Build a helper that summarizes older turns.

## Interview questions
- Why is chat memory important in conversational agents?
- How can memory become stale?
- What is the difference between short-term and long-term memory?
