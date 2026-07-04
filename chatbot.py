"""
=========================================================
Project : Rule-Based AI Chatbot
Internship : DecodeLabs Artificial Intelligence Internship
Author : Harsh

Description:
This is the main program for the Rule-Based AI Chatbot.
It controls the complete conversation flow between the
user and the chatbot.

Features:
- Continuous conversation using while loop
- Input sanitization
- Dictionary-based response lookup
- Unknown input handling
- Exit command handling
=========================================================
"""

# Import the predefined responses dictionary
from responses import responses


# Display the welcome message
print("=" * 60)
print("        Welcome to the Rule-Based AI Chatbot 🤖")
print("=" * 60)
print("Hello! I am your Rule-Based AI Chatbot.")
print("I can answer simple predefined questions.")
print("Type 'help' to know what I can do.")
print("Type 'bye', 'exit', or 'quit' to end the conversation.")
print("=" * 60)
print()


# Start the chatbot
while True:

    # Take input from the user
    user_input = input("You: ")

    # Clean the user input
    user_input = user_input.lower().strip()

    # Get the chatbot response
    bot_response = responses.get(
        user_input,
        "I'm sorry, I don't understand that. Please try another question."
    )

    # Display chatbot response
    print(f"Bot: {bot_response}")
    print()

    # Exit the chatbot
    if user_input in {"bye", "exit", "quit"}:
        print("Thank you for using the Rule-Based AI Chatbot.")
        print("Have a wonderful day! 👋")
        break
    