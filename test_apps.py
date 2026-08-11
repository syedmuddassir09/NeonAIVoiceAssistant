from brain.response import get_response


commands = [
    "open youtube",
    "open whatsapp",
    "open github",
    "open google",
    "open gmail",
    "open chatgpt",
    "open chrome",
    "open vs code",
    "open notepad",
    "open calculator",
    "open file explorer"
]


for command in commands:

    print("COMMAND:", command)

    response = get_response(command)

    print("NEON:", response)
    print()