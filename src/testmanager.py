from concurrent.futures import thread
import keyboard
import mouse
from interface.dofus_overlay import DofusOverlay
from threading import Thread

class TestManager(Thread):
    def __init__(self,iterface=None):
        Thread.__init__(self)
        self.mode = "combat"
        self.dofus_handler = None
        self.interface = interface
        self.order = ["panda","sadi","elio","iop"]
        self.i = 0
        
        #binding events
        keyboard.on_press_key("²", lambda _: self._switch_mode())
        keyboard.on_press_key("Tab", lambda _: self._switch_win())
        mouse.on_click(lambda : self._on_click())

    def _switch_win(self):
        if(self.mode == "combat"):
            print('press tab')
            self.interface.update_perso(self.order[self.i])
            self.i = (self.i+1)%len(self.order)

    def _switch_mode(self):
        if(self.mode=="combat"):
            self.mode = "hors_combat"
        elif(self.mode=="hors_combat"):
            self.mode = "combat"
        self.interface.update_mode(self.mode)
        print("mode : ",self.mode)
            
    def _on_click(self):
        if(self.mode == "hors_combat"):
            print("click")
            
    def run(self):
        #wait for end of program
        keyboard.wait("ESC")
        self.interface.overlay.quit()
        
if __name__ == "__main__":
    interface = DofusOverlay()
    m = TestManager(interface)
    m.start()
    interface.mainloop()
    m.join()  