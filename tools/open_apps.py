import os
import webbrowser


def open_app(command):
    """
    Open applications and websites based on voice command.
    """

    command = command.lower().strip()

    # =========================
    # WEBSITES
    # =========================

    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp."

    elif "github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub."

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail."

    elif "chatgpt" in command:
        webbrowser.open("https://chatgpt.com")
        return "Opening ChatGPT."

    # =========================
    # APPLICATIONS
    # =========================

    elif "chrome" in command:
        os.system("start chrome")
        return "Opening Chrome."

    elif "vs code" in command or "visual studio code" in command:
        os.system("code")
        return "Opening Visual Studio Code."

    elif "notepad" in command:
        os.system("notepad")
        return "Opening Notepad."

    elif "calculator" in command or "calc" in command:
        os.system("calc")
        return "Opening Calculator."

    elif "file explorer" in command or "explorer" in command:
        os.system("explorer")
        return "Opening File Explorer."

    return None