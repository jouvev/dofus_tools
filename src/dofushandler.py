import win32gui
import json

INI = "initiative.json"

def windowEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    if ("- dofus" in name.lower()):
        top_windows.append((hwnd, name))

class DofusHandler:
    def __init__(self):
        self.reset_win()
        if(len(self)==0):
            raise RuntimeError("No dofus window found")
        self.curr_hwnd = self.get_hwnd(0)
            
    def sort_win(self):
        self.dofus_hwnd.sort(key=lambda x: self.hwnd_ini[x],reverse=True)
        
    def reset_win(self):
        self.dofus_win = []
        win32gui.EnumWindows(windowEnumerationHandler, self.dofus_win)
        
        self.name_ini = json.load(open(INI))
        self.hwnd_ini = dict()
        
        self.dofus_hwnd = []
        
        for hwnd,win_name in self.dofus_win:
            for n in self.name_ini.keys():
                if n in win_name:
                    self.dofus_hwnd.append(hwnd)
                    self.hwnd_ini[hwnd] = self.name_ini[n]
                    break
                
        self.sort_win()
        
    def get_name_in_order(self):
        return [self.get_perso_name(self.get_hwnd(i)) for i in range(len(self))]
        
    def get_index_from_hwnd(self,hwnd):
        return self.dofus_hwnd.index(hwnd)
        
    def get_hwnd(self,i):
        return self.dofus_hwnd[i]
        
    def get_next_hwnd(self):
        curr = self.get_curr_hwnd()
        i = (self.get_index_from_hwnd(curr)+1) % len(self.dofus_hwnd)
        return self.dofus_hwnd[i]
    
    def get_previous_hwnd(self):
        curr = self.get_curr_hwnd()
        i = (self.get_index_from_hwnd(curr)-1) % len(self.dofus_hwnd)
        return self.dofus_hwnd[i]
    
    def get_curr_hwnd(self):
        tmp = win32gui.GetForegroundWindow()
        if(tmp in self.dofus_hwnd):
            self.curr_hwnd = tmp
        return self.curr_hwnd
        
    def __len__(self):
        return len(self.dofus_hwnd)