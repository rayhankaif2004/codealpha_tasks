import random
import datetime

responses = {
    "hello": ["Hi there!", "Hello! How can I help you today?", "Hey! Good to see you."],
    "hi": ["Hello!", "Hi! What's up?", "Hey there!"],
    "how are you": ["I'm doing great, thanks!", "I'm fine, thanks for asking.", "All good here!"],
    "what is your name": ["I'm a simple chatbot.", "You can call me ChatBot.", "I am your friendly chatbot."],
    "what time is it": ["The current time is {}."],
    "what is the date": ["Today's date is {}."],
    "tell me a joke": ["Why did the computer show up at work late? It had a hard drive!", "Why was the robot so bad at soccer? Because it kept stopping to recharge."],
    "thank you": ["You're welcome!", "No problem!", "Glad I could help."],
    "thanks": ["Anytime!", "Happy to help.", "You got it."],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

fallback_responses = [
    "Sorry, I don't understand. Can you try a different question?",
    "I'm not sure how to answer that yet.",
    "Can you say that in another way?"
]

available_questions = [
    "hello",
    "hi",
    "how are you",
    "what is your name",
    "what time is it",
    "what is the date",
    "tell me a joke",
    "thank you",
    "thanks",
    "bye"
]


def format_response(key):
    message = random.choice(responses[key])
    if key == "what time is it":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return message.format(now)
    if key == "what is the date":
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        return message.format(today)
    return message


def chatbot():
    print("Simple Chatbot")
    print("Type 'help' for a list of questions I can answer.")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").strip().lower()

        if not user:
            print("Bot: Please type a question or 'help'.")
            continue

        if user in responses:
            response = format_response(user)
            print(f"Bot: {response}")
            if user == "bye":
                break
        elif user in {"what's the time", "whats the time"}:
            print(f"Bot: The current time is {datetime.datetime.now().strftime('%H:%M:%S')}.")
        elif user in {"what's the date", "whats the date"}:
            print(f"Bot: Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}.")
        elif user in {"list", "options", "show questions"}:
            print("Bot: I can answer these questions:")
            for question in available_questions:
                print(f" - {question}")
        elif user == "help":
            print("Bot: Try asking one of the following:")
            for question in available_questions:
                print(f" - {question}")
        else:
            print(f"Bot: {random.choice(fallback_responses)}")


# Call the function
chatbot()