import win32gui
from threading import Thread, Lock
import time
import win32process
import psutil
from src.dofus.dofus import Dofus

def windowEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    _,pid = win32process.GetWindowThreadProcessId(hwnd)
    exe = psutil.Process(pid).exe()
    visible = win32gui.IsWindowVisible(hwnd)
    if("dofus 2" in name.lower() and "dofus.exe" in exe.lower() and visible):
        top_windows.append(hwnd)

class DofusHandler(Thread):
    """
    Class qui gere les id des fenetres dofus (hwnd)
    
    event : update_hwnd
    
    """
    def __init__(self):
        Thread.__init__(self)
        self.curr_hwnd = 0
        self.running = True
        self.dofus_hwnd = [Dofus(hwnd) for hwnd in self._get_win()]
        self.lock = Lock()
        self.observers = {
            "update_hwnd" : []
        }
        self.name_order = []
        
    def stop(self):
        self.running = False
        
    def add_observer(self,eventtype,callback):
        if(eventtype in self.observers):
            self.observers[eventtype].append(callback)
        else:
            raise RuntimeError("Event type not found : "+eventtype," in DofusHandler")
        
    def update_order(self,order):
        self.lock.acquire()
        
        new_order = [self.dofus_hwnd[self.get_index_from_hwnd(hwnd)] for hwnd in order]
        #ajoute les fenetres qui n'ont pas été ajoutées
        for d in self.dofus_hwnd:
            if d.hwnd not in [d.hwnd for d in new_order]:
                new_order.append(d)
        
        self.dofus_hwnd = new_order
        self.lock.release()
        self.notify("update_hwnd")
        
    def _get_win(self):
        tmp = []
        win32gui.EnumWindows(windowEnumerationHandler, tmp)
        return tmp
    
    def add_win(self,hwnd):
        self.lock.acquire()
        
        if hwnd not in [d.hwnd for d in self.dofus_hwnd]:
            self.dofus_hwnd.append(Dofus(hwnd))
            
            self.lock.release()
            self.notify("update_hwnd")
            return True
        
        self.lock.release()
        return False
        
    def is_dofus_window(self,hwnd):
        return hwnd in [d.hwnd for d in self.dofus_hwnd]
    
    def get_name(self,hwnd):
        hwnds = [d.hwnd for d in self.dofus_hwnd]
        return self.dofus_hwnd[hwnds.index(hwnd)].name
    
    def get_hwnd_by_name(self,name):
        namelist = self.get_name_in_order()
        return self.dofus_hwnd[namelist.index(name)].hwnd
        
    def get_name_in_order(self):
        return [d.name for d in self.dofus_hwnd]
        
    def get_index_from_hwnd(self,hwnd):
        return [d.hwnd for d in self.dofus_hwnd].index(hwnd)
        
    def get_hwnd(self,i):
        return self.dofus_hwnd[i].hwnd
        
    def get_next_hwnd(self):
        curr = self.get_curr_hwnd()
        i = (self.get_index_from_hwnd(curr)+1) % len(self.dofus_hwnd)
        return self.dofus_hwnd[i].hwnd
    
    def get_previous_hwnd(self):
        curr = self.get_curr_hwnd()
        i = (self.get_index_from_hwnd(curr)-1) % len(self.dofus_hwnd)
        return self.dofus_hwnd[i].hwnd
    
    def get_curr_hwnd(self):
        tmp = win32gui.GetForegroundWindow()
        if(self.is_dofus_window(tmp)):
            self.curr_hwnd = tmp
        return self.curr_hwnd
    
    def __len__(self):
        return len(self.dofus_hwnd)
    
    def remove_win(self,hwnd):
        self.lock.acquire()
        i = self.get_index_from_hwnd(hwnd)
        self.dofus_hwnd.pop(i)
        self.lock.release()
        self.notify("update_hwnd")
        
    def notify(self,eventtype):
        for f in self.observers[eventtype]:
            f([d.hwnd for d in self.dofus_hwnd],self.get_name_in_order())
    
    def run(self):
        while self.running :
            hwnd_tmp = self._get_win()
            
            #test si les fenetres ont été fermées
            for hwnd in [d.hwnd for d in self.dofus_hwnd]:
                if hwnd not in hwnd_tmp:
                    self.remove_win(hwnd)
                    print("Fenetre fermee :",hwnd)
                    
            #test si des fenetres ont été ouvertes
            for hwnd in hwnd_tmp:
                if(self.add_win(hwnd)):
                    print("new dofus window :",hwnd,"name :",self.get_name(hwnd))

            up = False
            for d in self.dofus_hwnd:
                d.update_port()
                if(d.update_name()):
                    up = True
            if(up):
                self.notify("update_hwnd")
            
            tmp_name_order = self.get_name_in_order()
            if(tmp_name_order != self.name_order):
                self.notify("update_hwnd")
                self.name_order = self.get_name_in_order()

            time.sleep(0.3)