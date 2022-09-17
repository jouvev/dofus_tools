import psutil
import win32gui
import win32process

def windowEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    if ("dofus 2" in name.lower()):
        top_windows.append((hwnd, name))
        
        
top_window = []

win32gui.EnumWindows(windowEnumerationHandler, top_window)

print(top_window)

for h,name in top_window:
    _,pid = win32process.GetWindowThreadProcessId(h)
    exe = psutil.Process(pid).exe()
    print(h,name,pid,exe)