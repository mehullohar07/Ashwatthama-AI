import subprocess
#import webbrowser


apps = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "vscode": "Code.exe",
    "instagram": "https://www.instagram.com",
    "youtube": "https://www.youtube.com"
}

def open_app(app_name):
    if app_name in apps:
        subprocess.Popen(apps[app_name])
    else:
        print(f"Application '{app_name}' not found.")
