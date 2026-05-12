"""
Task 1: Rule Based Chatbot
CodSoft AI Internship

This is a simple chatbot made using Python if-elif logic.
I customized the replies and added a small loop for conversation practice.
"""

def get_bot_reply(message):
    # converting user message to lowercase to compare easily
    message = message.lower().strip()

    if message in ["hi", "hello", "hey"]:
        return "Hello! I am a simple rule-based chatbot. How can I help you?"

    elif "your name" in message or "who are you" in message:
        return "I am StudentBot, a basic chatbot created using Python rules."

    elif "internship" in message:
        return "This chatbot is created as part of my AI internship task."

    elif "python" in message:
        return "Python is a beginner-friendly programming language used in AI and automation."

    elif "college" in message:
        return "College projects help students understand programming concepts practically."

    elif "help" in message:
        return "You can ask me about Python, internship, college, or AI basics."

    elif "ai" in message or "artificial intelligence" in message:
        return "AI means making computers perform tasks that normally need human intelligence."

    elif "thank" in message:
        return "You are welcome!"

    elif message in ["bye", "exit", "quit"]:
        return "Goodbye! Thanks for chatting."

    else:
        return "Sorry, I did not understand that. Please try asking in simple words."


def run_chatbot():
    print("======================================")
    print("        SIMPLE RULE BASED CHATBOT")
    print("======================================")
    print("Type 'bye', 'exit', or 'quit' to stop.\n")

    while True:
        user_text = input("You: ")
        reply = get_bot_reply(user_text)
        print("Bot:", reply)

        if user_text.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    run_chatbot()
