import subprocess
import webbrowser

apps = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "vscode": "Code.exe",
    "calculator": "calc.exe",
    "instagram": "https://www.instagram.com",
    "youtube": "https://www.youtube.com",
}


def open_app(app_name):
    if app_name not in apps:
        print(f"Application '{app_name}' not found.")
        return

    app = apps[app_name]

    if app.startswith(("http://", "https://")):
        webbrowser.open(app)
    else:
        try:
            subprocess.Popen(app)
        except OSError as error:
            print(f"Could not open {app_name}: {error}")
