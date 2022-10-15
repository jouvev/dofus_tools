import win32gui
from threading import Thread, Lock
import time
import win32process
import psutil
from src.dofus.dofus import Dofus
from src.tools.observer import Observer
import logging


class DofusHandler(Thread,Observer):
    """
    Class qui gere les id des fenetres dofus (hwnd) et leur ordre
    
    event : update_hwnd
    """
    def __init__(self):
        Thread.__init__(self)
        Observer.__init__(self,["update_hwnd"])  
        self.curr_hwnd = 0
        self.running = True
        self.dofus = [Dofus(hwnd) for hwnd in self._get_win()]
        for d in self.dofus:
            d.add_observer("fight",self.update_order)
        self.lock = Lock()
        self.name_order = []
        
    def get_hwnds(self):
        return [d.hwnd for d in self.dofus]
    
    def get_pids(self):
        return [d.pid for d in self.dofus]
    
    def get_names(self):
        return [d.name for d in self.dofus]
    
    def get_ports(self):
        return [d.port for d in self.dofus]
        
    def stop(self):
        self.running = False
        
    def update_order(self,order):
        self.lock.acquire()
        
        new_order = [self.dofus[self.get_index_by_hwnd(hwnd)] for hwnd in order]
        #ajoute les fenetres qui n'ont pas été ajoutées
        for d in self.dofus:
            if d.hwnd not in [d.hwnd for d in new_order]:
                new_order.append(d)
        
        self.dofus = new_order
        self.lock.release()
        self.notify("update_hwnd",self.get_hwnds(),self.get_names())
        
    def _get_win(self):
        tmp = []
        win32gui.EnumWindows(dofusEnumerationHandler, tmp)
        return tmp
    
    def add_win(self,hwnd):
        self.lock.acquire()
        if hwnd not in self.get_hwnds():
            d = Dofus(hwnd)
            self.dofus.append(d)
            d.add_observer("fight",self.update_order)
            
            self.lock.release()
            logging.info("new dofus window detected")
            self.notify("update_hwnd",self.get_hwnds(),self.get_names())
            return True
        
        self.lock.release()
        return False
        
    def is_dofus_window(self,hwnd):
        return hwnd in self.get_hwnds()
    
    def get_hwnd_by_name(self,name):
        namelist = self.get_names()
        return self.dofus[namelist.index(name)].hwnd
        
    def get_index_by_hwnd(self,hwnd):
        return self.get_hwnds().index(hwnd)
    
    def get_dofus_by_port(self,port):
        for d in self.dofus:
            d.update_port()
        return self.dofus[self.get_ports().index(port)]
        
    def get_next_dofus(self):
        curr = self.get_curr_hwnd()
        i = (self.get_index_by_hwnd(curr)+1) % len(self.dofus)
        return self.dofus[i]
    
    def get_previous_dofus(self):
        curr = self.get_curr_hwnd()
        i = (self.get_index_by_hwnd(curr)-1) % len(self.dofus)
        return self.dofus[i]
    
    def get_current_dofus(self):
        hwnd = self.get_curr_hwnd()
        return self.dofus[self.get_index_by_hwnd(hwnd)]
    
    def get_curr_hwnd(self):
        tmp = win32gui.GetForegroundWindow()
        if(self.is_dofus_window(tmp)):
            self.curr_hwnd = tmp
        return self.curr_hwnd
    
    def __len__(self):
        return len(self.dofus)
    
    def remove_win(self,hwnd):
        self.lock.acquire()
        logging.info("dofus window removed")
        i = self.get_index_by_hwnd(hwnd)
        self.dofus.pop(i)
        self.lock.release()
        self.notify("update_hwnd",self.get_hwnds(),self.get_names())
    
    def run(self):
        while self.running :
            hwnd_tmp = self._get_win()
            
            #test si les fenetres ont été fermées
            for hwnd in self.get_hwnds():
                if hwnd not in hwnd_tmp:
                    self.remove_win(hwnd)
                    
            #test si des fenetres ont été ouvertes
            for hwnd in hwnd_tmp:
                self.add_win(hwnd)

            up = False
            for d in self.dofus:
                d.update_port()
                if(d.update_name()):
                    up = True
            if(up):
                self.notify("update_hwnd",self.get_hwnds(),self.get_names())
            
            tmp_name_order = self.get_names()
            if(tmp_name_order != self.name_order):
                self.notify("update_hwnd",self.get_hwnds(),self.get_names())
                self.name_order = self.get_names()

            time.sleep(0.3)
            
def dofusEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    _,pid = win32process.GetWindowThreadProcessId(hwnd)
    exe = psutil.Process(pid).exe()
    visible = win32gui.IsWindowVisible(hwnd)
    if("dofus 2" in name.lower() and "dofus.exe" in exe.lower() and visible):
        top_windows.append(hwnd)