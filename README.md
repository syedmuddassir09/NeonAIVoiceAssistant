# 🤖 NEON — Personal AI Voice Assistant

NEON is a personal AI voice assistant built with Python.

The project is being developed step by step to create an assistant that can listen to voice commands, understand them, remember user information, respond using speech, and eventually control applications and other tools on the computer.

## 🚀 Project Goal

The long-term goal of NEON is to become a personal desktop AI assistant that can:

* 🎤 Listen to voice commands
* 🧠 Understand natural language
* 🔊 Respond using voice
* 💾 Remember user information
* 👋 Respond when called by the wake word **"NEON"**
* 🖥️ Open applications
* 🌐 Open websites
* 🔎 Search the web
* 📂 Work with files
* ⚙️ Control system functions
* 🤖 Use an LLM for intelligent conversations
* 🛠️ Execute tools based on user commands

## 🏗️ Current Architecture

```text
                    🎤 Microphone
                         │
                         ▼
                  Speech Recognition
                         │
                         ▼
                    🧠 NEON Brain
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
         💾 Memory              🛠️ Tools
              │                     │
              └──────────┬──────────┘
                         ▼
                    📝 Response
                         │
                         ▼
                    🔊 Text-to-Speech
                         │
                         ▼
                    🖥️ User
```

## 📁 Project Structure

```text
NEON/
│
├── .venv/                  # Python virtual environment
│
├── assets/                 # Project assets
│
├── brain/                  # NEON's decision-making logic
│   └── response.py
│
├── memory/                 # Persistent user memory
│   ├── memory.py
│   └── user_memory.json
│
├── tools/                  # System and application tools
│
├── voice/                  # Voice input/output
│   ├── listen.py
│   └── speak.py
│
├── main.py                 # Main application
├── test_voice.py           # Voice testing
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignored files
```

## 🎤 Voice Input

NEON uses Python speech recognition to convert microphone input into text.

Example:

```text
🎤 User: My name is Mudassir

You: my name is mudassir
```

The recognized text is then passed to NEON's brain for processing.

## 🔊 Voice Output

NEON uses `pyttsx3` for text-to-speech.

Example:

```text
NEON: Hello! I am NEON. How can I help you?
```

The response is printed to the terminal and spoken through the computer's speakers.

## 💾 Memory System

NEON has a persistent memory system.

For example, when the user says:

```text
My name is Mudassir
```

NEON stores the information in:

```text
memory/user_memory.json
```

Example:

```json
{
    "name": "Mudassir"
}
```

Later, the user can ask:

```text
What is my name?
```

NEON retrieves the stored information and responds.

## 🧠 Brain

The current NEON brain is rule-based.

It can recognize commands such as:

```text
Hello
Hi
What is your name?
My name is Mudassir
What is my name?
What time is it?
Stop
Exit
```

The current system uses Python conditions to determine the appropriate response.

The next major upgrade is to replace the rule-based system with an LLM-powered brain.

## 💤 Wake Word

NEON is being developed to work in a wake-word mode.

The intended behavior is:

```text
😴 NEON sleeping...

You: Hello

NEON: [ignores]

You: Hey NEON

NEON: Yes, I'm listening.

You: Open Chrome

NEON: [processes command]
```

The keyword **"NEON"** will be used to activate the assistant.

The wake-word system is currently under development.

## 🛠️ Technology Stack

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Main programming language |
| SpeechRecognition   | Speech-to-text            |
| pyttsx3             | Text-to-speech            |
| JSON                | Persistent memory         |
| Git                 | Version control           |
| GitHub              | Project hosting           |
| Virtual Environment | Dependency isolation      |

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/syedmuddassir09/NEON.git
```

Enter the project:

```bash
cd NEON
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run NEON:

```powershell
python main.py
```

## 🧪 Testing

Voice output can be tested using:

```powershell
python test_voice.py
```

The memory system can also be tested independently.

## 🗺️ Development Roadmap

### ✅ Completed

* [x] Python project structure
* [x] Virtual environment
* [x] Voice input
* [x] Voice output
* [x] Basic command processing
* [x] User memory
* [x] Persistent JSON memory
* [x] Basic voice assistant loop
* [x] Git repository
* [x] GitHub repository

### 🔄 In Progress

* [ ] Reliable wake-word detection
* [ ] "Hey NEON" interaction
* [ ] Natural language understanding
* [ ] Application launcher
* [ ] Website launcher

### 🔜 Planned

* [ ] LLM integration
* [ ] Tool calling
* [ ] Web search
* [ ] File management
* [ ] Windows system control
* [ ] Personalized preferences
* [ ] Conversation history
* [ ] Better long-term memory
* [ ] Vision capabilities
* [ ] More natural TTS
* [ ] Fully hands-free operation

## 🎯 Vision

NEON is not intended to remain a simple command-based chatbot.

The goal is to develop it into a personal AI agent capable of understanding natural language, remembering the user, using tools, controlling the computer, and interacting naturally through voice.

```text
                 🤖 NEON

          "Your Personal AI Assistant"

                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Voice       Memory       AI
        │           │           │
        └───────────┼───────────┘
                    │
                  Tools
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Apps        Web          Files
```

## 👨‍💻 Author

**Syed Mudassir**

NEON is a continuously evolving personal AI assistant project built for learning, experimentation, and practical AI development.

---

⭐ If you find this project interesting, consider starring the repository.
