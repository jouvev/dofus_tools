import keyboard
import mouse
import logging
import time
import win32gui
import win32com.client
from src.tools.observer import Observer
from src.command.command import Command
from src.dofus.dofus import Dofus

class DofusManager(Observer):
    def __init__(self,config,dofus_handler):
        super().__init__(["stop","update_mode","open_console"])
        self.config = config
        self.mode = "combat"
        self.dofus_handler = dofus_handler
        self.running = True
        self.confirm = False
        self.cmdobject = Command(self.dofus_handler)
        
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        
        #events binding
        keyboard.add_hotkey(config["keyboard_bindings"]['switch_mode'], lambda : self._switch_mode())
        keyboard.add_hotkey(config["keyboard_bindings"]['next_win'], lambda : self._switch_next_win())
        keyboard.add_hotkey(config["keyboard_bindings"]['prev_win'], lambda : self._switch_previous_win())
        keyboard.add_hotkey(config["keyboard_bindings"]['stop'], lambda : self._stop())
        keyboard.add_hotkey(config["keyboard_bindings"]['open_console'], lambda : self.open_console())
        #keyboard.on_press_key(config["keyboard_bindings"]['left'], lambda e: self.change_map("left",e))
        #keyboard.on_press_key(config["keyboard_bindings"]['right'], lambda e: self.change_map("right",e))
        #keyboard.on_press_key(config["keyboard_bindings"]['up'], lambda e: self.change_map("up",e))
        #keyboard.on_press_key(config["keyboard_bindings"]['down'], lambda e: self.change_map("down",e))
        mouse.on_click(lambda : self._click())
        
    def open_console(self):
        self.notify("open_console",self.cmdobject)
        
    def change_map(self,dir,e):
        if(self.allow_event() and not e.is_keypad):
            if(self.mode=="hors_combat"):
                for d in self.dofus_handler.dofus:
                    self.executor.submit(lambda dof : dof.change_map(dir),d)
            else:
                self.dofus_handler.get_current_dofus().change_map(dir)
        
    def _click(self):
        if(self.allow_event() and self.mode=="hors_combat"):
            x,y = win32gui.GetCursorPos()
            delay = not keyboard.is_pressed(self.config["keyboard_bindings"]['click_no_delay'])
            curr_h = win32gui.GetForegroundWindow()
            for d in self.dofus_handler.selected:
                if(d.hwnd != curr_h):
                    realx,realy = win32gui.ScreenToClient(d.hwnd,(x,y))
                    d.do_async_action(Dofus.click,realx,realy,delay)
        
    def allow_event(self):
        tmp = win32gui.GetForegroundWindow()
        return self.dofus_handler.is_dofus_window(tmp)

    def _stop(self):
        if( not self.allow_event()):
            return
        logging.info("Stopping all")
        self.running = False
        self.notify("stop")
        
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
        self.notify("update_mode",self.mode)