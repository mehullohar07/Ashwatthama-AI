# Ashwatthama AI

A Python-based personal AI assistant that combines voice commands, desktop automation, and AI-powered conversational responses. Built as a step-by-step learning project focused on practical AI engineering and modular software development.

**Current Version:** `v0.4`

## Features

- AI-powered conversational responses using the Groq API
- Text-based interaction mode
- Voice-based command input
- Text-to-speech responses
- Launch supported Windows applications
- Open supported websites such as YouTube and Instagram
- Display the current date and time
- Handle predefined commands and general AI queries
- Modular Python project structure

## Tech Stack

- **Language:** Python
- **AI Integration:** Groq API
- **Configuration:** Environment variables using `python-dotenv`
- **Voice Input:** SpeechRecognition
- **Text-to-Speech:** pyttsx3
- **Interface:** Command-line interface

## Project Structure

```text
Ashwatthama-AI/
├── core/
│   ├── assistant.py
│   └── command_handler.py
├── modules/
│   ├── apps.py
│   ├── llm.py
│   ├── system.py
│   ├── utility.py
│   └── voice.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3
- A Windows computer for the supported desktop commands
- A microphone for voice input
- A Groq API key for AI-powered responses

### 1. Clone the repository

```bash
git clone https://github.com/mehullohar07/Ashwatthama-AI.git
cd Ashwatthama-AI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own key.

**Security:** Never upload `.env` or expose your API key publicly. Keep `.env` in `.gitignore`. If sharing the project, provide a `.env.example` containing only placeholder values.

### 4. Run Ashwatthama AI

```bash
python main.py
```

Select the available interaction mode and start using the assistant.

## Version History

### v0.4
- Integrated the Groq API for AI-powered responses.
- Added text and voice interaction modes.
- Connected AI responses with the existing command handler.
- Preserved predefined commands alongside conversational AI.

### v0.3.1
- Added microphone-based speech recognition.
- Updated the runtime dependency list.
- Updated the assistant banner and version output.

### v0.3
- Added text-to-speech responses using `pyttsx3`.
- Added the version command.
- Consolidated application commands.
- Introduced the voice module.

### v0.2
- Organized the project into `core/` and `modules/`.
- Separated command handling, application actions, and utilities.

### v0.1
- Initial command-line assistant.

## Roadmap

- **v0.5:** Desktop graphical interface using Tkinter
- **v0.6:** Tool calling and more capable command execution
- **v0.7:** Memory features
- **v0.8:** Retrieval-Augmented Generation (RAG)
- **v0.9:** FastAPI integration
- **v0.10:** Docker support
- **v1.0:** Advanced agentic AI capabilities

*Roadmap items represent planned development, not features already released.*

## Author

**Mehul Lohar**

- GitHub: https://github.com/mehullohar07

---

Ashwatthama AI is an evolving personal AI assistant project built to explore Python, AI integration, automation, and practical software engineering.
