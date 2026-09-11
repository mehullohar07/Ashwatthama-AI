from core.command_handler import *
from core.assistant import banner

banner()

while True:
    command = input("\nYou:").lower().strip()

    if command == "exit":
        print("Goodbye!!")
        break

    execute_command(command)
