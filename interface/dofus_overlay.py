from interface.overlay import OverlayFactory
import json
import tkinter as tk
from PIL import Image,ImageTk

class DofusOverlay:
    def __init__(self,order):
        self.overlay = OverlayFactory().make_overlay()
        self.img = json.load(open("config.json"))['img']
        self.perso = dict()
        
        self.curr_mode = ""
        self.curr_perso = ""
        
        for n in order:
            path = self.img[n]
            img = ImageTk.PhotoImage(Image.open(path).resize((70,70)))
            f = tk.Label(self.overlay,image=img)
            f.image = img
            f.pack(side="left",padx=5, pady=5)
            self.perso[n] = f
        
        frame_mode = tk.Frame(self.overlay)
        frame_mode.pack(side="left",padx=5, pady=5)
        
        img = ImageTk.PhotoImage(Image.open("img\\combat.png").resize((30,30)))
        f = tk.Label(frame_mode,image=img)
        f.image = img
        f.pack(side="top",padx=0, pady=0)
        self.combat = f
        
        img = ImageTk.PhotoImage(Image.open("img\\hors_combat.jpg").resize((30,30)))
        f = tk.Label(frame_mode,image=img)
        f.image = img
        f.pack(side="top",padx=0, pady=0)
        self.hors_combat = f
            
    def update_perso(self,name):
        for n in self.perso.keys():
            if(n==name):
                self.perso[n].config(borderwidth=2, relief="solid")
            else:
                self.perso[n].config(borderwidth=2, relief="flat")
        self.overlay.update()
        self.curr_perso = name
        
    def update_mode(self,mode):
        if(mode=="combat"):
            self.combat.config(borderwidth=2, relief="solid")
            self.hors_combat.config(borderwidth=2, relief="flat")
        else:
            self.hors_combat.config(borderwidth=2, relief="solid")
            self.combat.config(borderwidth=2, relief="flat")
        self.overlay.update()
        self.curr_mode = mode
        
    def mainloop(self):
        self.overlay.mainloop()

if __name__=='__main__':
    order = ["Nighwin",
    "Jeandou" ,
    "Xox-elie" ,
    "Syllafarmn"]
    DofusOverlay(order=order).mainloop()