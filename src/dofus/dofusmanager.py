import keyboard
import mouse
import win32gui
import win32com.client
from concurrent.futures import ThreadPoolExecutor

class DofusManager:
    def __init__(self,config,dofus_handler):
        self.config = config
        self.mode = "combat"
        self.dofus_handler = dofus_handler
        self.running = True
        self.observers = {
            "stop" : []
        }
        self.confirm = False
        self.executor = ThreadPoolExecutor(4)
        
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        
        #events binding
        keyboard.add_hotkey(config["keyboard_bindings"]['switch_mode'], lambda : self._switch_mode())
        keyboard.add_hotkey(config["keyboard_bindings"]['next_win'], lambda : self._switch_next_win())
        keyboard.add_hotkey(config["keyboard_bindings"]['prev_win'], lambda : self._switch_previous_win())
        keyboard.add_hotkey(config["keyboard_bindings"]['stop'], lambda : self._stop())
        mouse.on_click(lambda : self._click())
        
    def _click(self):
        if(self.allow_event() and self.mode=="hors_combat"):
            x,y = win32gui.GetCursorPos()
            curr_h = win32gui.GetForegroundWindow()
            for d in self.dofus_handler.dofus:
                if(d.hwnd != curr_h):
                    realx,realy = win32gui.ScreenToClient(d.hwnd,(x,y))
                    self.executor.submit(lambda dof,i,j : dof.click(i,j),d,realx,realy)
        
    def allow_event(self):
        tmp = win32gui.GetForegroundWindow()
        return self.dofus_handler.is_dofus_window(tmp)

    def _stop(self):
        if( not self.allow_event()):
            return
        for callback in self.observers["stop"]:
            callback()
        self.running = False
        
    def add_observer(self,event,callback):
        self.observers[event].append(callback)

    def _switch_previous_win(self):
        if( not self.allow_event()):
            return
        d = self.dofus_handler.get_previous_dofus()
        d.open()

    def _switch_next_win(self):
        if( not self.allow_event()):
            return
        d = self.dofus_handler.get_next_dofus()
        d.open()

    def _switch_mode(self):
        if( not self.allow_event()):
            return
        if(self.mode=="combat"):
            self.mode = "hors_combat"
        elif(self.mode=="hors_combat"):
            self.mode = "combat"