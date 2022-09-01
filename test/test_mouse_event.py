from pynput.mouse import Listener, Controller, Button
import time
import win32gui
import win32com.client

def on_click(x, y, button, pressed):
    global i
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        print(i)
        time.sleep(0.5)
        hwnd = top_windows[i][0]
        win32gui.SetForegroundWindow(hwnd)
        """#mouse.move(x,y)
        mouse.press(Button.left)
        mouse.release(Button.left)"""
        print("next")
        i+=1
        i%=len(top_windows)
    
def windowEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    if ("- dofus" in name.lower()):
        top_windows.append((hwnd, name))
    
if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    print(top_windows)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    
    win32gui.SetForegroundWindow(top_windows[0][0])
    
    i=1
    mouse = Controller()
    
    with Listener(on_click=on_click) as listener:
        listener.join()