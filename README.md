# Ashwatthama AI 🤖

A lightweight command-line personal assistant built with Python. It can run desktop commands, report the current date and time, and respond using text-to-speech.

**Latest release:** [v0.3](https://github.com/mehullohar07/Ashwatthama-AI/releases/tag/v0.3)

## Features

- Launch commonly used Windows applications: Chrome, Visual Studio Code, Paint, and Notepad
- Open YouTube and Instagram commands
- Tell the current date and time
- Answer basic assistant commands such as `hello`, `creator`, and `who are you?`
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
│   └── voice.py            # Text-to-speech support
├── main.py                 # Application entry point
└── README.md
```

## Getting started

### Requirements

- Python 3
- Windows, for the current desktop application commands
- `pyttsx3` for text-to-speech

### Installation

```bash
git clone https://github.com/mehullohar07/Ashwatthama-AI.git
cd Ashwatthama-AI
pip install pyttsx3
python main.py
```

Type `help` after startup to see the available commands.

## Version history

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

- Voice input and speech recognition
- Weather information
- Web search
- AI-powered integrations

## Author

Created by [Mehul Lohar](https://github.com/mehullohar07).
