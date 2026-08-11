import pyttsx3


def speak(text):

    print("🔊 NEON speaking:", text)

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    # Use Microsoft David
    engine.setProperty("voice", voices[0].id)

    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()

    engine.stop()