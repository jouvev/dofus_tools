from dofushandler import Hwnd
import win32com.client
import win32gui
import time
import keyboard

class GestionCombat:
    def __init__(self):
        self.dofus_hwnd = Hwnd()
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
    
    def open(self,i):
        process_id = self.dofus_hwnd.get_hwnd(i)
        win32gui.ShowWindow(process_id,5)
        win32gui.SetForegroundWindow(process_id)
    
    def next(self):
        process_id = self.dofus_hwnd.get_next_hwnd()
        win32gui.ShowWindow(process_id,5)
        win32gui.SetForegroundWindow(process_id)
        
    def run(self):
        self.open(0)
        while True:
            if keyboard.is_pressed('Tab'):
                self.next()
                time.sleep(0.5)
            #if keyboard.is_pressed('q'):
            #    break
            #if keyboard.is_pressed('r'):
            #    self.dofus_hwnd.reset_win()
            #    self.open(0)
            #    time.sleep(0.5)