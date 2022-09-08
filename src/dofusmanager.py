import keyboard
import mouse
from src.dofushandler import DofusHandler
import win32gui
import time

class DofusManager:
    def __init__(self):
        self.mode = "hors_combat"
        self.dofus_handler = DofusHandler()
        
        #binding events
        keyboard.on_press_key("²", lambda _: self._switch_mode())
        keyboard.on_press_key("Tab", lambda _: self._switch_win())
        mouse.on_click(lambda : self._on_click())

    def _switch_win(self):
        if(self.mode == "combat"):
            print('press tab')
            self._open_next()
            
    def _open_next(self):
        hwnd = self.dofus_handler.get_next_hwnd()
        win32gui.ShowWindow(hwnd,4)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.1)

    def _switch_mode(self):
        if(self.mode=="combat"):
            self.mode = "hors_combat"
        elif(self.mode=="hors_combat"):
            self.mode = "combat"
        print("mode : ",self.mode)
            
    def _on_click(self):
        if(self.mode == "hors_combat"):
            print("click")
            posx,posy = mouse.get_position()
            for _ in range(len(self.dofus_handler)):
                self._open_next()
                mouse.move(posx,posy)
                mouse.click()
            
    def run(self):
        #wait for end of program
        keyboard.wait("ESC")
        print("END")
        
if __name__ == "__main__":
    DofusManager().run()