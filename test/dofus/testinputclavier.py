import keyboard
import win32gui,win32process,win32con,win32api
import psutil
import time

def dofusEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    _,pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid < 0:
        return
    exe = psutil.Process(pid).exe()
    visible = win32gui.IsWindowVisible(hwnd)
    if("dofus 2" in name.lower() and "dofus.exe" in exe.lower() and visible):
        top_windows.append(hwnd)
        
def click(hwnd,x,y):
    x,y = win32gui.ScreenToClient(hwnd,(x,y))
    lParam = win32api.MAKELONG(x, y)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)
    
def press_key(hwnd,key):
    win32gui.SendMessage(hwnd, win32con.WM_CHAR, ord(key), 0)
    
def press_enter(hwnd):
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    
def write(hwnd,text):
    for c in text:
        press_key(hwnd,c)
        
tmp = []
win32gui.EnumWindows(dofusEnumerationHandler, tmp)
print(tmp)
hwnd = tmp[0]

#click(hwnd,116,1028)

write(hwnd,"h")



input("Press any key to exit...")