from datetime import datetime


def get_response(command):
    """
    Decide NEON's response based on user command.
    """

    command = command.lower()

    if "hello" in command or "hi" in command:
        return "Hello! I am NEON. How can I help you?"

    elif "your name" in command:
        return "My name is NEON. I am your personal AI assistant."

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"

    elif "exit" in command or "stop" in command:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I am still learning. I don't understand that yet."