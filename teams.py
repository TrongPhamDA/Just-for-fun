import subprocess

def install_module(module):
    print(f"Installing {module}...")
    subprocess.run(["pip", "install", module])

try:
    import time
except ImportError:
    install_module("time")
    import time

try:
    import pyautogui
except ImportError:
    install_module("pyautogui")
    import pyautogui

try:
    import keyboard
except ImportError:
    install_module("keyboard")
    import keyboard

def start_application(interval):
    print("Program starting...")
    for i in range(10, 0, -1):
        print(f"{i} seconds until start...")
        time.sleep(1)
    count = 1
    while True:
        if keyboard.is_pressed('esc') or keyboard.is_pressed('pause'):
            break
        pyautogui.press('win')
        pyautogui.typewrite('TEAMS')
        time.sleep(2)
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'e')
        time.sleep(2)
        pyautogui.typewrite('SEARCH SOMEONE')
        pyautogui.press('delete', presses=14)
        print(f"Iteration {count} completed.")
        count += 1
        for j in range(interval):
            if keyboard.is_pressed('esc') or keyboard.is_pressed('pause'):
                break
            time.sleep(1)

start_application(300)

"""
install Python
run CMD and run teams.py
"""