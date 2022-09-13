from threading import Thread
import time

class Listener(Thread):
    def __init__(self,manager,interface):
        Thread.__init__(self)
        self.manager = manager
        self.interface = interface
        
    def run(self):
        print("listener started")
        while self.manager.running:
            curr_perso = self.manager.dofus_handler.get_perso_name(self.manager.dofus_handler.get_curr_hwnd())
            inter_perso = self.interface.curr_perso
            if ( curr_perso != inter_perso):
                self.interface.update_perso(curr_perso)
                
            curr_mode = self.manager.mode
            inter_mode = self.interface.curr_mode
            if ( curr_mode != inter_mode):
                self.interface.update_mode(curr_mode)
                
            time.sleep(0.1)
          
        print("listener stopped")
        
               

           