import tkinter as tk

class Overlay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-alpha',0.8)
        self.attributes('-topmost', True)
        self.geometry('44x84+0+0')
        self.wm_resizable(False, False)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>',self.clickwin)
        self.bind('<B1-Motion>',self.dragwin)
        
    def dragwin(self,event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x,y=y))

    def clickwin(self,event):
        self._offsetx = event.x
        self._offsety = event.y
    