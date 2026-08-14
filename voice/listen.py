import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import tempfile
import os


def listen(silent=False):
    """
    Record voice from microphone and convert it into text.

    silent=True:
        Used while NEON is waiting for the wake word.
        No unnecessary messages are printed.

    silent=False:
        Used after NEON is activated.
        Shows listening messages.
    """

    sample_rate = 40000
    duration = 8

    if not silent:
        print("🎤 NEON is listening... Speak now!")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    if not silent:
        print("🧠 Understanding...")

    filename = None

    try:
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

        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)

        if not silent:
            print(f"You: {text}")

        return text.lower().strip()

    except sr.UnknownValueError:

        if not silent:
            print("NEON: I didn't understand.")

        return ""

    except sr.RequestError:

        if not silent:
            print("NEON: Speech service unavailable.")

        return ""

    finally:

        if filename and os.path.exists(filename):
            os.remove(filename)