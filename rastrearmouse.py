import pyautogui

def posicao():
    return pyautogui.position()

while True:
    print(posicao())