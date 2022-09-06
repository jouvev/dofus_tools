import win32gui
import json

INI = "initiative.json"

def windowEnumerationHandler(hwnd, top_windows):
    name = win32gui.GetWindowText(hwnd)
    if ("- dofus" in name.lower()):
        top_windows.append((hwnd, name))

class Hwnd:
    def __init__(self):
        self.reset_win()
            
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
        
        self.i = 0
        
    def get_hwnd(self,i):
        return self.dofus_hwnd[i]
        
    def get_next_hwnd(self):
        res = self.dofus_hwnd[self.i]
        self.i += 1
        self.i %= len(self.dofus_hwnd)
        return res
        
    def __len__(self):
        return len(self.dofus_hwnd)