from threading import Thread
import logging
import time
import win32gui

class Listener(Thread):
    def __init__(self,manager,interface):
        Thread.__init__(self,name="Listener")
        self.manager = manager
        self.interface = interface
        self.is_visible = True
        
    def run(self):
        while self.manager.running:
            if(not self.interface.is_running):
                time.sleep(0.3)
                continue
            
            curr_hwnd = self.manager.dofus_handler.get_curr_hwnd()
            inter_hwnd = self.interface.curr_hwnd
            if ( curr_hwnd != inter_hwnd): 
                self.interface.update_perso(curr_hwnd)
                
            hwnd = win32gui.GetForegroundWindow()
            if(not self.manager.dofus_handler.is_dofus_window(hwnd) and int(self.interface.frame(),base=16) != int(hwnd) and self.is_visible):
                self.interface.withdraw()
                self.is_visible = False
            elif(self.manager.dofus_handler.is_dofus_window(hwnd) and not self.is_visible):
                self.interface.deiconify()
                self.is_visible = True
            
            time.sleep(0.3)
        logging.info("Listener stopped")
              
        
               

           