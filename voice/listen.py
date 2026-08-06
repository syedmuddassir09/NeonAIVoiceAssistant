import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import tempfile
import os


def listen():
    """
    Record voice from microphone and convert it into text.
    """

    sample_rate = 44100
    duration = 8

    print("🎤 NEON is listening... Speak now!")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    print("🧠 Understanding...")

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as file:

        filename = file.name

    write(
        filename,
        sample_rate,
        audio
    )

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)

        print(f"You: {text}")

        return text.lower()

    except sr.UnknownValueError:
        print("NEON: I didn't understand.")
        return ""

    except sr.RequestError:
        print("NEON: Speech service unavailable.")
        return ""

    finally:
        os.remove(filename)