import tkinter as tk

class OverlayFactory:
    def make_overlay(self,posx,posy):
        overlay = tk.Tk()
        overlay.attributes('-alpha',0.8)
        overlay.attributes('-topmost', True)
        overlay.geometry('44x84+'+str(posx)+"+"+str(posy))
        overlay.wm_resizable(False, False)
        overlay.overrideredirect(True)
        return overlay
    