import win32process
import win32gui
import win32api
import win32con
import psutil
import time
from threading import Lock
import random

class Dofus:
    def __init__(self,hwnd):
        self.hwnd = hwnd
        _,self.pid = win32process.GetWindowThreadProcessId(hwnd)
        self.set_name()
        self.set_port()
        self.confirm = False
        self.lock = Lock()
        
    def set_name(self):
        name = win32gui.GetWindowText(self.hwnd)
        lname = name.split(" - ")
        if(len(lname) == 1):
            self.name = ""
        else:
            self.name = lname[0]
        
    def set_port(self):
        self.port = ""
        p = psutil.Process(self.pid)
        for conn in p.connections():
            if conn.raddr.port == 5555 :
                self.port = str(conn.laddr.port)
                break
            
    def get_infos(self):
        return self.hwnd, self.pid, self.name, self.port
    
    def update_name(self):
        tmp_name = self.name
        self.set_name()
        return tmp_name != self.name
    
    def update_port(self):
        tmp_port = self.port
        self.set_port()
        return tmp_port != self.port
    
    def open(self):
        win32gui.ShowWindow(self.hwnd,3)
        win32gui.SetForegroundWindow(self.hwnd)
        
    def click(self,x,y):
        with self.lock:
            lParam = win32api.MAKELONG(x, y)
            ntry = 0
            time.sleep(random.random()*0.3+0.2)
            self.confirm = False
            while not self.confirm and ntry < 3:
                ntry += 1
                win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
                win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, None, lParam)
                time.sleep(1)
                if(self.confirm):
                    break
        