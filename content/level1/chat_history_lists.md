# Lists for Chat History

## Concept explanation
A list is an ordered collection of items. In AI applications, lists are useful for storing a conversation history as a sequence of turns.

## Real-world AI use case
A support copilot can keep a list of user and assistant messages so it can track context over several exchanges.

## Execution flow
1. Create a list of conversation turns.
2. Store each turn as a dictionary with speaker and text.
3. Iterate through the list and print each message.
4. Use the list to simulate a conversation memory.

## Run this concept locally
1. Open a terminal in the repository root.
2. Run the example with:
   ```bash
   python content/level1/chat_history_lists.py
   ```
3. The script will print the conversation history as a list of turns.

## Exercises
- Add a third turn to the history.
- Change the assistant response style.
- Print only the user messages.

## Interview questions
- Why is a list a good fit for chat history?
- How does this differ from using a single string?
- What happens if the history grows very large?
