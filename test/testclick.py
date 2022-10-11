import mouse
import pyautogui

mouse.on_click(lambda : print(pyautogui.position()))

input()