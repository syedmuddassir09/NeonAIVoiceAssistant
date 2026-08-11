# 🤖 NEON — Your Personal Voice-Controlled AI Assistant

NEON is a **Python-based personal AI assistant** designed to interact with and control your computer through voice commands.

The goal of NEON is to make computer interaction more natural by allowing you to communicate with your PC using your voice. As the project develops, NEON will become capable of understanding natural-language commands, using APIs, performing computer tasks, and assisting with everyday activities.

> 🚧 **Current Status:** Basic voice-controlled version working — actively under development.

---

## ✨ Features

### 🎤 Voice Interaction

* Listen to user voice commands.
* Convert speech into text.
* Process commands through the NEON system.

### 🧠 Command Processing

* Process user commands.
* Detect the NEON wake word.
* Detect sleep and exit commands.
* Route commands through the assistant's response system.

### 🔊 Voice Response

* NEON can respond to the user using text-to-speech.

### 💤 Sleep Mode

NEON can temporarily stop listening when the user says commands such as:

* `wait`
* `stop`
* `go to sleep`
* `sleep`
* `that's all`

### 🔴 Exit Commands

NEON can be completely stopped using commands such as:

* `shutdown neon`
* `exit neon`
* `quit neon`

---

## 📂 Project Structure

```text
NEON/
│
├── main.py
│
├── voice/
│   ├── listen.py
│   └── speak.py
│
├── brain/
│   └── response.py
│
└── README.md
```

### 📁 `main.py`

The main entry point of NEON.

It connects the different components and controls the overall assistant workflow.

### 📁 `voice/`

Contains the voice-related components.

#### `listen.py`

Handles listening to the user's voice and converting it into a command.

#### `speak.py`

Handles NEON's voice responses using text-to-speech.

### 📁 `brain/`

Contains the logic responsible for processing commands and generating responses.

#### `response.py`

Processes the user's command and determines the appropriate response.

---

## ▶️ How NEON Works

The basic workflow is:

```text
       🎤 User Voice
            │
            ▼
      ┌─────────────┐
      │   Listen    │
      └──────┬──────┘
             │
             ▼
      ┌─────────────┐
      │    Brain    │
      │   Process   │
      └──────┬──────┘
             │
             ▼
      ┌─────────────┐
      │   Response  │
      └──────┬──────┘
             │
             ▼
       🔊 NEON Voice
```

---

## 💬 Usage Examples

### Start NEON

Run the main Python file:

```bash
python main.py
```

NEON starts listening for commands.

### Wake Command

```text
User: "Neon"
```

NEON recognizes its wake word and begins processing commands.

### Sleep

```text
User: "Go to sleep"
```

NEON enters sleep mode.

### Stop

```text
User: "Stop"
```

NEON stops processing commands temporarily.

### Exit

```text
User: "Shutdown Neon"
```

NEON shuts down completely.

---

## 🛠️ Technologies

* **Python**
* **Speech Recognition**
* **Text-to-Speech**
* **Python Modules**
* **AI / LLM Integration** *(planned)*
* **API Integration** *(planned)*

---

## 🚀 Future Goals

NEON is currently in its basic stage. Planned improvements include:

* 🧠 AI-powered natural-language command understanding
* 🔌 Dynamic API integration
* 🖥️ PC application control
* 🌐 Web and browser automation
* 📁 File and folder management
* ⚙️ System controls
* 💾 Personal memory
* 🎤 Improved voice recognition
* 🔊 More natural AI responses
* 🧩 Tool-based command execution
* 🤖 Intelligent task automation

The long-term goal is to turn NEON into a powerful personal AI assistant capable of understanding natural language and performing real tasks on the user's PC.

---

## 👨‍💻 Project

**NEON — Your Personal Voice-Controlled AI Assistant**

Built with **Python** and developed incrementally while learning and experimenting with voice technology, AI, automation, APIs, and computer interaction.

---

## 📌 Development Status

NEON is an ongoing personal project.

The current version focuses on building the core voice-assistant architecture. New capabilities will be added progressively as the project evolves.
