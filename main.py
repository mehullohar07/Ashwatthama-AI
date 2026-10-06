from core.command_handler import *
from core.assistant import banner
from modules.voice import take_command

banner()

while True:

    command = take_command()

    if command == "":
        continue

    if command == "exit":
        print("Goodbye!!")
        break

    execute_command(command)