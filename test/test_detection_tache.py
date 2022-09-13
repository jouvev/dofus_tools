import win32gui
import win32api
import pyautogui
import win32com.client
import time

def windowEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    if ("- dofus" in name.lower()):
        top_windows.append((hwnd, name))
    
if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    print(top_windows)
    """for i in top_windows:
        print(i)
        win32gui.ShowWindow(i[0],1)S
        win32gui.SetForegroundWindow(i[0])"""

    i = 0
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    hwnd = top_windows[i][0]
    win32gui.ShowWindow(hwnd,5)
    win32gui.SetForegroundWindow(hwnd)
    
    while True:
        if(win32api.GetKeyState(0x01)<0):
            x,y = pyautogui.position()
            print("detection x,y : ",x,y)
            for i in range(len(top_windows)):
                hwnd = top_windows[i][0]
                win32gui.ShowWindow(hwnd,5)
                win32gui.SetForegroundWindow(hwnd)
                
                time.sleep(0.05)
                print('click',i)
                pyautogui.click(x,y,clicks=2)
                
        if(win32api.GetKeyState(0x02)<0):
            break