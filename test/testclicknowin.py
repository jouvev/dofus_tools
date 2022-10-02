import win32api
import win32con
import win32gui 

def click(x, y):
    hWnd = win32gui.FindWindow(None, "Spotify Premium")
    print(hWnd)
    lParam = win32api.MAKELONG(x, y)

    hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)
    
click(10,500)