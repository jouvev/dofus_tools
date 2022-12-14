import win32gui
from threading import Thread, Lock
import time
import win32process
import psutil
from src.dofus.dofus import Dofus
from src.tools.observer import Observer
import logging
import pyautogui

logger = logging.getLogger(__name__)

class DofusHandler(Thread,Observer):
    """
    Class qui gere les id des fenetres dofus (hwnd) et leur ordre
    
    event : update_hwnd
    """
    def __init__(self):
        Thread.__init__(self)
        Observer.__init__(self,["update_hwnd","new_select_list","houseevent"])
        self.curr_hwnd = None
        self.running = True
        self.dofus = [Dofus(hwnd) for hwnd in self._get_win()]
        for d in self.dofus:
            d.add_observer("fight",self.update_order)
            d.add_observer("house",self.houseevent)
        self.lock = Lock()
        self.name_order = []
        self.selected = [d for d in self.dofus]
        
    def houseevent(self):
        self.notify("houseevent")
        
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
        for d in self.dofus:
            d.stop()
            
    def add_select(self,hwnd):
        d = self.dofus[self.get_index_by_hwnd(hwnd)]
        if(d not in self.selected):
            self.selected.append(d)
        else:
            self.selected.remove(d)
        self.notify("new_select_list",[d.hwnd for d in self.selected])
        
    def update_order(self,order):
        self.lock.acquire()
        
        new_order = [self.dofus[self.get_index_by_name(name)] for name in order if name in self.get_names()]
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
            d.add_observer("house",self.houseevent)
            self.selected.append(d)
            self.notify("new_select_list",[d.hwnd for d in self.selected])
            
            self.lock.release()
            logger.info("new dofus window detected")
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

    def get_index_by_name(self,name):
        namelist = self.get_names()
        return namelist.index(name)
    
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
        if(hwnd is None):
            return None
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
        logger.info("dofus window removed")
        i = self.get_index_by_hwnd(hwnd)
        d = self.dofus.pop(i)
        self.selected.remove(d)
        self.notify("new_select_list",[d.hwnd for d in self.selected])
        d.stop()
        del d
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
                if(d.update_name()):
                    up = True
                d.update_port()
            if(up):
                logger.info(f"dofus window name updated {self.get_names()}")
                self.notify("update_hwnd",self.get_hwnds(),self.get_names())
            
            tmp_name_order = self.get_names()
            if(tmp_name_order != self.name_order):
                self.notify("update_hwnd",self.get_hwnds(),self.get_names())
                self.name_order = self.get_names()

            time.sleep(0.3)
            
        logger.info("dofus window handler stopped")
    
    def execute(self,cmd,arg):
        logger.info(f"execute cmd : {cmd}, args : {arg}")
        if(cmd == "goto"):
            curr_dof = self.get_current_dofus()
            if(curr_dof):
                curr_dof.do_async_action(Dofus.goto,*arg)
                return "ok"
            else:
                return "no dofus window selected"
        elif(cmd == "stoptravel"):
            curr_dof = self.get_current_dofus()
            if(curr_dof):
                curr_dof.do_async_action(Dofus.stoptravel)
                return "ok"
            else:
                return "no dofus window selected"
        elif(cmd == "gotos"):
            for d in self.selected:
                d.do_async_action(Dofus.goto,*arg)
            return "ok"
        elif(cmd == "stoptravels"):
            for d in self.selected:
                d.do_async_action(Dofus.stoptravel)
            return "ok"
        elif(cmd == "clickcell"):
            curr_dof = self.get_current_dofus()
            if(curr_dof):
                curr_dof.do_async_action(Dofus.click_cell,*arg)
                return f"click on cellid {arg[0]}"
            else:
                return "no dofus window selected"
        elif(cmd == "zaap"):
            curr_dof = self.get_current_dofus()
            if(curr_dof):
                nom = " ".join(arg)
                curr_dof.do_async_action(Dofus.zaap,nom)
                return "ok"
            else:
                return "no dofus window selected"
        elif(cmd == "zaaps"):
            nom = " ".join(arg)
            for d in self.selected:    
                d.do_async_action(Dofus.zaap,nom)
            return "ok"
        elif(cmd == "group"):
            curr_dof = self.get_current_dofus()
            if(curr_dof):
                listinv = [n for n in self.get_names() if n != curr_dof.name and n != ""]
                if(len(listinv) == 0):
                    return "no other dofus window"
                curr_dof.do_async_action(Dofus.invite,listinv)
                return f"invite {listinv}"
            else:
                return "no dofus window selected"
        elif(cmd == "reset"):
            curr_dof = self.get_current_dofus()
            if(curr_dof):
                self.remove_win(curr_dof.hwnd)
                return f"{curr_dof.name} reset"
            else:
                return "no dofus window selected"
        elif(cmd == "flagcalibrage"):
            curr_dof = self.get_current_dofus()
            #normalement une chasse doit être lancée sinon t'es con
            if(curr_dof):
                if(curr_dof.chasseObject is not None):
                    pos = pyautogui.locateCenterOnScreen('ressources\\img\\hintflag.png',confidence=0.9)
                    if(pos is not None):
                        x,y = pos
                    else : 
                        return "Flag not found\n/!\ attention à ne pas cacher le flag avec la fenêtre de commande"
                    y = y - 30*(len(curr_dof.chasseObject.listindice)-1)
                    for d in self.dofus:
                        if(d.chasseObject is not None):
                            d.chasseObject.set_flag_pos(x,y)
                    return f"Flag on {x},{y}"
                else:
                    return "Une chasse doit être lancée"
            else:
                return "no dofus window selected"
       
def dofusEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    _,pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid < 0:
        return
    exe = psutil.Process(pid).exe()
    visible = win32gui.IsWindowVisible(hwnd)
    if("dofus 2" in name.lower() and "dofus.exe" in exe.lower() and visible):
        top_windows.append(hwnd)