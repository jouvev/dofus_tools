from threading import Thread
import logging
import time
import win32gui

class Listener(Thread):
    def __init__(self,manager,interface):
        Thread.__init__(self)
        self.manager = manager
        self.interface = interface
        self.is_visible = True
        
    def run(self):
        while self.manager.running:
            curr_hwnd = self.manager.dofus_handler.get_curr_hwnd()
            inter_hwnd = self.interface.curr_hwnd
            if ( curr_hwnd != inter_hwnd): 
                self.interface.update_perso(curr_hwnd)
                
            if(not self.manager.dofus_handler.is_dofus_window(win32gui.GetForegroundWindow())):
                self.interface.withdraw()
                self.is_visible = False
            else:
                if(not self.is_visible):
                    self.interface.deiconify()
            
            time.sleep(0.3)
        logging.info("Listener stopped")
              
        
               

           