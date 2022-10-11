import win32process
import win32gui
import win32api
import win32con
import psutil
import time
from threading import Lock
import random
import keyboard
import pyautogui

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
            
    def change_map(self,direction):
        if(direction == "left"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(280,426))
            self.click(realx,realy)
        elif(direction == "right"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(1617,614))
            self.click(realx,realy)
        elif(direction == "down"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(844,915))
            self.click(realx,realy)
        elif(direction == "up"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(866,28))
            self.click(realx,realy)
            
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
        
    def click(self,x,y,delay=True):
        with self.lock:
            lParam = win32api.MAKELONG(x, y)
            if(delay):
                time.sleep(random.random())
            win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
            win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, None, lParam)
        
    def cmd_zaap(self,dest):
        print("go to",dest)
        self.open()
        time.sleep(1)
        keyboard.send('h')
        time.sleep(1)
        pyautogui.click(x=560, y=432)
        time.sleep(1)
        for k in dest:
            keyboard.send(k)
        time.sleep(1)
        pyautogui.doubleClick(x=742, y=323)