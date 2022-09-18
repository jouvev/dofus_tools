import psutil
import win32gui
import win32process
import time
from interface.overlay import OverlayFactory
from threading import Thread
import random

class tmp(Thread):
    def __init__(self,overlay):
        Thread.__init__(self)
        self.overlay = overlay
    
    def run(self):
        top_window = []

        win32gui.EnumWindows(windowEnumerationHandler, top_window)
        while(True):
            pos = win32gui.GetWindowPlacement(top_window[0][0])
            x,y = pos[-1][0],pos[-1][1]
            h,l = random.randint(80,500),random.randint(80,500)
            self.overlay.geometry(str(h)+'x'+str(l)+'+'+str(x)+'+'+str(y))

def windowEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    _,pid = win32process.GetWindowThreadProcessId(hwnd)
    exe = psutil.Process(pid).exe()
    visible = win32gui.IsWindowVisible(hwnd)
    if("dofus.exe" in exe.lower() and visible):
        top_windows.append((hwnd, name))
        
overlay = OverlayFactory().make_overlay()

possniffer = tmp(overlay)
possniffer.start()

overlay.mainloop()
