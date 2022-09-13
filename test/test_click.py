import win32api
import pyautogui
import time

while True:
    if(win32api.GetKeyState(0x01)<0):
        x,y = pyautogui.position()
        for _ in range(3):
            print('next')
            time.sleep(0.1)
            print("click",x,y)
            time.sleep(0.02)
        print("retour sur la fenetre originale")
    time.sleep(0.1)