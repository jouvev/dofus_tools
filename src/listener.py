from threading import Thread
import time

class Listener(Thread):
    def __init__(self,manager,interface):
        self.manager = manager
        self.interface = interface
        
    def run(self):
        while self.manager.running:
            curr_perso = self.manager.handler.get_perso_name(self.manager.handler.get_curr_hwnd())
            inter_perso = self.interface.curr_perso
            if ( curr_perso != inter_perso):
                self.interface.update_perso(curr_perso)
            
            curr_mode = self.manager.mode
            inter_mode = self.interface.curr_mode
            if ( curr_mode != inter_mode):
                self.interface.update_mode(curr_mode)
                
            time.sleep(0.1)
               

           