from datetime import datetime
from memory.memory import remember, recall
from tools.open_apps import open_app


def get_response(command):

    command = command.lower().strip()

    # Open applications/websites
    app_response = open_app(command)

    if app_response:
        return app_response

    # Greeting
    if "hello" in command or "hi" in command:
        return "Hello! I am NEON. How can I help you?"

    # NEON identity
    elif "your name" in command:
        return "My name is NEON. I am your personal AI assistant."

    # Remember user's name
    elif "my name is" in command:
        name = command.replace("my name is", "").strip()

        remember("name", name)

        return f"I will remember your name, {name}."

    # Recall user's name
    elif "what is my name" in command or "do you know my name" in command:
        name = recall("name")

        if name:
            return f"Your name is {name}."

        return "I don't know your name yet."

    # Time
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}"

    # Day
    elif "day" in command:
        current_day = datetime.now().strftime("%A")

        return f"Today is {current_day}"

    # Date
    elif "date" in command:
        current_date = datetime.now().strftime("%d %B %Y")

        return f"Today's date is {current_date}"

    # Unknown command
    else:
        return "Sorry, I am still learning. I don't understand that yet."