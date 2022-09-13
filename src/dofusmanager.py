from threading import Thread
import keyboard
import pyautogui
import win32api
from src.dofushandler import DofusHandler
import win32gui
import time
import win32com.client

class DofusManager(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.mode = "combat"
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        self.dofus_handler = DofusHandler()
        self.running = True
        
        #binding events
        keyboard.add_hotkey("²", lambda : self._switch_mode())
        keyboard.add_hotkey("Tab", lambda : self._switch_next_win())
        keyboard.add_hotkey("shift+Tab", lambda : self._switch_previous_win())
        keyboard.add_hotkey("ESC", lambda : self._stop())
        
        hwnd = self.dofus_handler.get_hwnd(0)
        self._open(hwnd)

    def _stop(self):
        self.running = False

    def _switch_previous_win(self):
        self._open_previous()
    
    def _open(self,hwnd):
        while hwnd != self.dofus_handler.get_curr_hwnd():
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(0.1)
          
    def _open_previous(self):
        hwnd = self.dofus_handler.get_previous_hwnd()
        self._open(hwnd)
    
    def _switch_next_win(self):
        self._open_next()
            
    def _open_next(self):
        hwnd = self.dofus_handler.get_next_hwnd()
        self._open(hwnd)

    def _switch_mode(self):
        if(self.mode=="combat"):
            self.mode = "hors_combat"
        elif(self.mode=="hors_combat"):
            self.mode = "combat"
        print("mode : ",self.mode)
            
    def run(self):
        while self.running:
            if(self.mode=="hors_combat" and win32api.GetKeyState(0x01)<0):
                x,y = pyautogui.position()
                time.sleep(0.3)
                for _ in range(len(self.dofus_handler)-1):
                    self._open_next()
                    time.sleep(0.1)#pause pour l'affichage
                    pyautogui.click(x,y)
                    time.sleep(0.02)#pause pour click
                self._open_next()
            time.sleep(0.05)#pause de la boucle
            
        print("stop")
        
if __name__ == "__main__":
    DofusManager().run()