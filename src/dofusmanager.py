from threading import Thread
import keyboard
import pyautogui
import win32api
from src.dofushandler import DofusHandler
import win32gui
import time
import win32com.client

class DofusManager(Thread):
    def __init__(self,config):
        Thread.__init__(self)
        self.config = config
        self.mode = "combat"
        self.dofus_handler = DofusHandler()
        self.running = True
        
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        
        #binding events
        keyboard.add_hotkey(config["keyboard_bindings"]['switch_mode'], lambda : self._switch_mode())
        keyboard.add_hotkey(config["keyboard_bindings"]['next_win'], lambda : self._switch_next_win())
        keyboard.add_hotkey(config["keyboard_bindings"]['prev_win'], lambda : self._switch_previous_win())
        keyboard.add_hotkey(config["keyboard_bindings"]['stop'], lambda : self._stop())
        
        hwnd = self.dofus_handler.get_hwnd(0)
        self._open(hwnd)
        
    def allow_event(self):
        tmp = win32gui.GetForegroundWindow()
        return self.dofus_handler.is_dofus_window(tmp)

    def _stop(self):
        if( not self.allow_event()):
            return
        self.running = False

    def _switch_previous_win(self):
        if( not self.allow_event()):
            return
        hwnd = self.dofus_handler.get_previous_hwnd()
        self._open(hwnd)
    
    def _open(self,hwnd):
        while hwnd != self.dofus_handler.get_curr_hwnd():
            win32gui.ShowWindow(hwnd,3)
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(0.1)
    
    def _switch_next_win(self):
        if( not self.allow_event()):
            return
        hwnd = self.dofus_handler.get_next_hwnd()
        self._open(hwnd)

    def _switch_mode(self):
        if( not self.allow_event()):
            return
        if(self.mode=="combat"):
            self.mode = "hors_combat"
        elif(self.mode=="hors_combat"):
            self.mode = "combat"
            
    def run(self):
        while self.running:
            if(self.allow_event() and self.mode=="hors_combat" and win32api.GetKeyState(0x01)<0):
                x,y = pyautogui.position()
                time.sleep(0.2)
                for _ in range(len(self.dofus_handler)-1):
                    self._switch_next_win()
                    time.sleep(0.1)#pause pour l'affichage
                    pyautogui.click(x,y)
                    time.sleep(0.02)#pause pour click
                self._switch_next_win()
            time.sleep(0.05)#pause de la boucle
        
if __name__ == "__main__":
    DofusManager().run()