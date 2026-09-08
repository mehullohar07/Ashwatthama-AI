from commands import *

ASSISTANT_NAME = "Ashwatth"

print(f"{ASSISTANT_NAME} Initialized...")

while True:
    command = input("How can I help you? ").lower()
    
    if command == "hello":
        greet()

    elif command == "bye":
        goodbye()

    elif command == "who are you":
       who_are_you()

    elif command == "creator":
        creator()

    elif command == "current time":
        current_time()

    elif command == "current date":
        current_date()

    elif command == "help":
        help_command()

    elif command == "version":
        version()

    elif command == "open notepad":
        open_notepad()

    elif command == "open calculator":
        open_calculator()

    elif command == "open chrome":
        open_chrome()

    elif command == "open paint":
        open_paint()

    elif command == "open vscode":
        open_vscode()

    elif command == "open youtube":
        open_youtube()

    elif command == "open instagram":
        open_instagram()

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Command not recognized")