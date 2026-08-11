import json
import os


MEMORY_FILE = "memory/user_memory.json"


def load_memory():
    """
    Load saved user information.
    """

    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return {}


def save_memory(data):
    """
    Save user information.
    """

    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def remember(key, value):
    """
    Store new information.
    """

    memory = load_memory()

    memory[key] = value

    save_memory(memory)


def recall(key):
    """
    Get stored information.
    """

    memory = load_memory()

    return memory.get(key, None)