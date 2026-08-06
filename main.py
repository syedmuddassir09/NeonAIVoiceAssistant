from voice.listen import listen
from voice.speak import speak
from brain.response import get_response


def main():

    speak("Hello! I am NEON. I am ready.")

    while True:

        command = listen()

        if command == "":
            continue

        response = get_response(command)

        speak(response)

        if "exit" in command or "stop" in command:
            break


if __name__ == "__main__":
    main()