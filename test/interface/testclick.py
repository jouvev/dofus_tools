import win32gui
import mouse

mouse.on_click(lambda : click())

def click():
    x,y = win32gui.GetCursorPos()
    print(x,y)
    
input()