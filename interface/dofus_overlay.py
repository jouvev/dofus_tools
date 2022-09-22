from interface.overlay import OverlayFactory
import tkinter as tk
from PIL import Image,ImageTk
from threading import RLock

class DofusOverlay:
    def __init__(self,config,order,order_name):
        self.overlay = OverlayFactory().make_overlay(config["overlay"]['posx'],config["overlay"]["posy"])
        self.overlay.bind("<<Destroy>>", lambda e: self.overlay.destroy())
        self.img = config['img']
        self.perso = dict()
        self.curr_order = []
        self.lock = RLock()
        
        self.frame_perso = tk.Frame(self.overlay)
        self.frame_perso.pack(side="left",padx=0, pady=0)
        
        self.curr_mode = ""
        self.curr_hwnd = 0
        
        self.update_order(order,order_name)
        
        frame_mode = tk.Frame(self.overlay)
        frame_mode.pack(side="left",padx=0, pady=0)
        
        img = ImageTk.PhotoImage(Image.open("img\\combat.png").resize((30,30)))
        f = tk.Label(frame_mode,image=img)
        f.image = img
        f.pack(side="top",padx=5, pady=3)
        self.combat = f
        
        img = ImageTk.PhotoImage(Image.open("img\\hors_combat.jpg").resize((30,30)))
        f = tk.Label(frame_mode,image=img)
        f.image = img
        f.pack(side="top",padx=5, pady=3)
        self.hors_combat = f
    
    def mainloop(self):
        self.overlay.mainloop()
            
    def update_perso(self,hwnd):
        self.lock.acquire()
        for h in self.perso:
            if(h==hwnd):
                self.perso[h].config(borderwidth=2, relief="solid")
            else:
                self.perso[h].config(borderwidth=2, relief="flat")
        self.overlay.update()
        self.curr_hwnd = hwnd
        self.lock.release()
        
    def update_mode(self,mode):
        self.lock.acquire()
        if(mode=="combat"):
            self.combat.config(borderwidth=2, relief="solid")
            self.hors_combat.config(borderwidth=2, relief="flat")
        else:
            self.hors_combat.config(borderwidth=2, relief="solid")
            self.combat.config(borderwidth=2, relief="flat")
        self.overlay.update()
        self.curr_mode = mode
        self.lock.release()

    def update_order(self,order,order_name):
        self.lock.acquire()
        self.perso = dict()
        lorder = len(order)
        l = lorder * 84 + 44 
        h = 84
        self.overlay.geometry(str(l)+"x"+str(h))
        
        #clear
        for child in self.frame_perso.winfo_children():
            child.destroy()
        self.frame_perso.config(width=1)
        
        #building new
        for hwnd,n in zip(order,order_name):
            if(n not in self.img):
                n = ""
            path = self.img[n]
            img = ImageTk.PhotoImage(Image.open(path).resize((70,70)))
            f = tk.Label(self.frame_perso,image=img)
            f.image = img
            f.pack(side="left",padx=5, pady=5)
            self.perso[hwnd] = f
        
        self.update_perso(self.curr_hwnd)
        self.overlay.update()
        self.lock.release()