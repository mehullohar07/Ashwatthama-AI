from modules.apps import *

from modules.utility import *

def execute_command(command):
    if command == "hello":
        greet()

    elif command == "creator":
        creator()

    elif command == "who are you?":
        who_are_you()

    elif command == "current time":
        current_time()

    elif command == "current date":
        current_date()

    elif command == "open chrome":
        open_chrome()

    elif command == "help":
        help_menu()

    elif command == "open paint":
        open_paint()

    elif command == "open vs code":
        open_vscode()

    elif command == "open notepad":
        open_notepad()

    elif command == "open instagram":
        open_instagram()

    elif command == "open youtube":
        open_youtube()

    elif command == "bye":
        goodbye()

    else:
        print("Sorry, I don't understand that command.")