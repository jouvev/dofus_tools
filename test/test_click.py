import win32api
import win32gui
import win32con
import mouse

hwnd = win32gui.GetForegroundWindow()

mouse.on_click(lambda : my_click(hwnd,0,100))

def my_click(hWnd,x, y):
    print("click")
    lParam = win32api.MAKELONG(x, y)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)
    
pause = input('Press enter to exit')