from datetime import datetime
from memory.memory import remember, recall
from tools.open_apps import open_app
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No Google/Gemini API key found in .env. Add GOOGLE_API_KEY or GEMINI_API_KEY.")


def get_response(command):

    command = command.lower().strip()

    # Open applications/websites
    # app_response = open_app(command)

    client = genai.Client(api_key=api_key)
    app_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=command
    )
    print(app_response.text)
    if app_response:
        return app_response.text

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