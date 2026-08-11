from voice.listen import listen
from voice.speak import speak
from brain.response import get_response


WAKE_WORD = "neon"

SLEEP_WORDS = [
    "Wait"
    "stop",
    "go to sleep",
    "sleep",
    "that's all",
    "thats all"
]

EXIT_WORDS = [
    "shutdown neon",
    "exit neon",
    "quit neon"
]


def is_sleep_command(command):
    command = command.lower().strip()
    return any(word in command for word in SLEEP_WORDS)


def is_exit_command(command):
    command = command.lower().strip()
    return any(word in command for word in EXIT_WORDS)


def main():

    print("=" * 50)
    print("🤖 NEON Voice Assistant")
    print("Say 'NEON' to wake me.")
    print("=" * 50)

    while True:

        # =====================================
        # SLEEP / WAKE-WORD MODE
        # =====================================

        command = listen(silent=True)

        if not command:
            continue

        command = command.lower().strip()

        # =====================================
        # COMPLETE SHUTDOWN
        # =====================================

        if is_exit_command(command):

            speak("Goodbye. NEON is shutting down.")

            print("🔴 NEON completely stopped.")

            return

        # =====================================
        # CHECK WAKE WORD
        # =====================================

        if WAKE_WORD not in command:
            continue

        # =====================================
        # WAKE UP
        # =====================================

        print("⚡ NEON ACTIVATED!")

        speak("Yes, I'm listening.")

        # =====================================
        # ACTIVE CONVERSATION
        # =====================================

        while True:

            command = listen()

            if not command:
                continue

            command = command.lower().strip()

            print("COMMAND RECEIVED:", command)

            # =================================
            # COMPLETE SHUTDOWN
            # =================================

            if is_exit_command(command):

                speak("Goodbye. NEON is shutting down.")

                print("🔴 NEON completely stopped.")

                return

            # =================================
            # GO BACK TO SLEEP
            # =================================

            if is_sleep_command(command):

                speak("Okay. I'll wait for you.")

                print("😴 NEON is waiting.")

                break

            # =================================
            # NORMAL COMMAND
            # =================================

            response = get_response(command)

            print("NEON:", response)

            speak(response)


if __name__ == "__main__":
    main()