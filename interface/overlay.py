import tkinter as tk

class OverlayFactory:
    def make_overlay(self):
        overlay = tk.Tk()
        overlay.attributes('-alpha',0.8)
        overlay.attributes('-topmost', True)
        overlay.geometry('390x80+0+0')
        overlay.wm_resizable(False, False)
        overlay.overrideredirect(True)
        return overlay
    
if __name__ == '__main__':
    overlay = OverlayFactory().make_overlay()
    overlay.mainloop()