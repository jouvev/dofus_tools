import tkinter as tk
from src.interface.commandinterface import CommandInterface

class CommandBouchon:
    def __init__(self):
        self.history = []
        
    def execute(self,cmd):
        self.history.append(cmd)
        return "ok"

if __name__ == "__main__":
    root =tk.Tk()
    CommandInterface(root,CommandBouchon())
    
    root.mainloop()