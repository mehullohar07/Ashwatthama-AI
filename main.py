from core.command_handler import *

from core.assistant import banner

from core.command_handler import execute_command

banner()

while True:
    command = input("\nYou:").lower().strip()

    if command == "exit":
        print("Goodbye!!")
        break

    execute_command(command)