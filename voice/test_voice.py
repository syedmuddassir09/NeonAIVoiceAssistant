import pyttsx3

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

for voice in voices:
    print(voice.id)

engine.say("Testing NEON voice")
engine.runAndWait()