# Ashwatthama AI 🤖

A lightweight, command-line personal assistant written in Python. Ashwatthama AI currently helps with simple desktop actions, browser shortcuts, and date/time utilities.

**Current release:** v0.2

## Features

### Launch applications
- Chrome
- Visual Studio Code
- Paint
- Notepad

### Open websites
- YouTube
- Instagram

### Utility commands
- `current time`
- `current date`

### Assistant commands
- `hello`
- `creator`
- `who are you?`
- `help`
- `bye`
- `exit`

## Project structure

```text
Ashwatthama-AI/
├── core/
│   ├── assistant.py        # Assistant identity and startup banner
│   └── command_handler.py  # Command routing
├── modules/
│   ├── apps.py             # Desktop and browser actions
│   ├── system.py           # Reserved for future system features
│   └── utility.py          # Greetings, help, date, and time utilities
├── main.py                 # Application entry point
├── README.md
└── LICENSE
```

## Getting started

### Requirements

- Python 3
- Windows, for the current desktop application shortcuts
- Chrome and Visual Studio Code available on your system if you plan to use their launch commands

### Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/mehullohar07/Ashwatthama-AI.git
   cd Ashwatthama-AI
   ```

2. Start the assistant:

   ```bash
   python main.py
   ```

3. Type a command when prompted—for example, `help`, `current time`, or `open youtube`. Type `exit` to close the assistant.

## Version history

### v0.2
- Reorganized the project into `core/` and `modules/`
- Separated command handling, application actions, and utility functions
- Improved project organization and command flow

### v0.1
- Initial command-line release

## Roadmap

- Voice input and speech recognition
- Text-to-speech responses
- Weather information
- Web search
- AI-powered integrations

## Author

Created by [Mehul Lohar](https://github.com/mehullohar07).

---

Ashwatthama AI is being developed step by step into a more capable personal assistant.
