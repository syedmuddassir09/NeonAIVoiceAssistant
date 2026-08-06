import pyttsx3


def speak(text: str):

    print(f"NEON: {text}")

    engine = pyttsx3.init("sapi5")

    voices = engine.getProperty("voices")

    # Select Microsoft Zira voice
    for voice in voices:
        if "Zira" in voice.name:
            engine.setProperty("voice", voice.id)
            break

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()

    engine.stop()