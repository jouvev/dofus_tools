import win32gui
import json

INI = "initiative.json"

def windowEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    if ("dofus 2" in name.lower()):
        top_windows.append((hwnd, name))

class DofusHandler:
    """
    Class qui gere les id des fenetres dofus (hwnd)
    
    """
    def __init__(self):
        self.reset_win()
        if(len(self)==0):
            raise RuntimeError("No dofus window found")
        self.curr_hwnd = 0
            
    def sort_win(self):
        self.dofus_hwnd.sort(key=lambda x: self.hwnd_ini[x],reverse=True)
        
    def update_order(self,order):
        for i in range(len(order)):
            n = order[i]
            hwnd = self.name_hwnd[n]
            self.hwnd_ini[hwnd] = -i
        self.sort_win()
        
    def reset_win(self):
        self.dofus_win = []
        win32gui.EnumWindows(windowEnumerationHandler, self.dofus_win)
        
        self.name_ini = json.load(open(INI))
        self.hwnd_ini = dict()
        self.hwnd_name = dict()
        self.name_hwnd = dict()
        
        self.dofus_hwnd = []
        
        for hwnd,win_name in self.dofus_win:
            for n in self.name_ini.keys():
                if n in win_name:
                    self.dofus_hwnd.append(hwnd)
                    self.hwnd_ini[hwnd] = self.name_ini[n]
                    self.hwnd_name[hwnd] = n
                    self.name_hwnd[n] = hwnd
                    break
                
        self.sort_win()
        
    def get_name_in_order(self):
        return sorted(list(self.name_ini.keys()),key=lambda x: self.name_ini[x],reverse=True)
        
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
        
    def get_perso_name(self,hwnd):
        return self.hwnd_name[hwnd]
    
    def __len__(self):
        return len(self.dofus_hwnd)
    
    
if __name__ == "__main__":
    dh = DofusHandler()