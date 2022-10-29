import pyautogui

x, y = pyautogui.locateCenterOnScreen('ressources\\img\\hintflag.png', confidence=0.9, grayscale=True)
print(x,y)