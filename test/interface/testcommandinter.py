import tkinter as tk
from src.interface.commandinterface import CommandInterface
import win32gui

class CommandBouchon:
    def __init__(self):
        self.history = []
        
    def execute(self,cmd):
        self.history.append(cmd)
        return "ok"
    
class TestCommandInterface(CommandInterface):
    def __init__(self,root,command):
        super().__init__(root,command)
        self.bind("<Button-1>",lambda e :self.onclick(e))
        
    def onclick(self,e):
        print("click",int(str(self.frame()),base=16),win32gui.GetForegroundWindow(),self.master.winfo_id())

if __name__ == "__main__":
    root =tk.Tk()
    ci = TestCommandInterface(root,CommandBouchon())
    root.mainloop()