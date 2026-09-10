import subprocess

import webbrowser

def open_chrome():
    subprocess.subprocess.Popen(["chrome.exe"])

def open_notepad():
    subprocess.subprocess.Popen(["notepad.exe"])

def open_paint():
    subprocess.subprocess.Popen(["mspaint.exe"])

def open_vscode():
    subprocess.subprocess.Popen(["Code.exe"])

def open_instagram():
    webbrowser.open("https://www.instagram.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")