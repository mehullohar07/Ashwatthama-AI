from  datetime import datetime

VERSION = "0.2"

def greet():
    print("Namaste Mehul! How can I assist you today?")

def goodbye():
    print("Goodbye! have a productive day ahead!")

def current_time():
    print("Current Time:", datetime.now().strftime("%H:%M:%S"))

def current_date():
    print("Current Date:", datetime.now().strftime("%d/%m/%Y"))

def creator():
    print("My creator is Mehul.")

def who_are_you():
    print("I am Ashwatth, your AI assistant.")

def help_menu():
    print("""
    =========================
            HELP MENU
    =========================

    APPLICATIONS
    ------------
    1. Open Chrome
    2. Open Paint
    3. Open VS Code
    4. Open Notepad
    5. Open Calculator
    6. Open Instagram
    7. Open YouTube

    UTILITY COMMANDS
    ----------------
    8. Current Time
    9. Current Date

    SYSTEM COMMANDS
    ---------------
    10. Hello
    11. creator
    12. Who are you?
    13. Help
    14. Version
    15. Exit
    """)