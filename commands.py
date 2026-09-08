import subprocess

import webbrowser

from datetime import datetime

def greet():
    print("Namaste!")

def goodbye():
    print("See you later! Have a great day!")

def who_are_you():
    print("I am Ashwatth, your AI assistant.")

def creator():
    print("My creator is Mehul.")

def version():
    print("Ashwatthama version 0.1")

def open_chrome():
    subprocess.Popen(["chrome.exe"])

def open_paint():
    subprocess.Popen(["mspaint.exe"])

def open_vscode():
    subprocess.Popen(["code.cmd"])

def open_notepad():
    subprocess.Popen(["notepad.exe"])

def open_calculator():
    subprocess.Popen(["calculator.exe"])

def current_time():
    now = datetime.now()
    print("Current Time:", now.strftime("%H:%M:%S"))

def current_date():
    today = datetime.now()
    print("Current Date:", today.strftime("%d/%m/%Y"))

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def help_command():
    print("""
    Available commands:
    Hello
    Bye
    Creator
    Help
    Current Time
    Current Date
    Exit
    Who Are You
    Version
    """)