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
        open_app("chrome")

    elif command == "help":
        help_menu()

    elif command == "open paint":
        open_app("paint")

    elif command == "open vscode":
        open_app("vscode")

    elif command == "open notepad":
        open_app("notepad")

    elif command == "open instagram":
        open_app("instagram")

    elif command == "open youtube":
        open_app("youtube")

    elif command == "version":
        version()

    elif command == "bye":
        goodbye()

    else:
        print("Sorry, I don't understand that command.")
