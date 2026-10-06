# Ashwatthama AI 🤖

A lightweight voice-enabled command-line personal assistant built with Python. It can run desktop commands, report the current date and time, listen for spoken commands, and respond using text-to-speech.

**Latest source version:** v0.3.1

## Features

- Launch commonly used Windows applications: Chrome, Visual Studio Code, Paint, and Notepad
- Open YouTube and Instagram commands
- Tell the current date and time
- Accept spoken commands through your microphone
- Read responses aloud with text-to-speech
- Show the installed assistant version with `version`

## Commands

| Command | Action |
| --- | --- |
| `hello` | Greets you |
| `creator` | Shows the creator |
| `who are you?` | Introduces the assistant |
| `current time` | Shows the current time |
| `current date` | Shows the current date |
| `open chrome` | Opens Chrome |
| `open vscode` | Opens Visual Studio Code |
| `open paint` | Opens Paint |
| `open notepad` | Opens Notepad |
| `open instagram` | Opens Instagram |
| `open youtube` | Opens YouTube |
| `version` | Shows the current version |
| `help` | Displays the command menu |
| `bye` | Says goodbye |
| `exit` | Closes the assistant |

## Project structure

```text
Ashwatthama-AI/
├── core/
│   ├── assistant.py        # Assistant name, version, and startup banner
│   └── command_handler.py  # Command routing
├── modules/
│   ├── apps.py             # Application and website command mapping
│   ├── system.py           # Reserved for future system features
│   ├── utility.py          # Assistant responses and utility commands
│   └── voice.py            # Text-to-speech and speech-to-text support
├── main.py                 # Application entry point
├── requirements.txt
└── README.md
```

## Getting started

### Requirements

- Python 3
- Windows, for the current desktop application commands
- A working microphone for voice commands

### Installation

```bash
git clone https://github.com/mehullohar07/Ashwatthama-AI.git
cd Ashwatthama-AI
pip install -r requirements.txt
python main.py
```

Type `help` after startup to see the available commands.

## Version history

### v0.3.1
- Added microphone-based speech-to-text command input with `SpeechRecognition`
- Added the required runtime dependency list
- Updated the assistant banner and `version` output to v0.3.1

### v0.3
- Added text-to-speech responses with `pyttsx3`
- Added the `version` command
- Consolidated application commands into a shared launcher
- Added the `voice.py` module

### v0.2
- Reorganized the project into `core/` and `modules/`
- Separated command handling, application actions, and utilities

### v0.1
- Initial command-line release

## Roadmap

- Weather information
- Web search
- AI-powered integrations

## Author

Created by [Mehul Lohar](https://github.com/mehullohar07).
