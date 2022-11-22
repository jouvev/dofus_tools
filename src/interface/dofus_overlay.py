from src.interface.commandinterface import CommandInterface
from tkinter import messagebox
from src.interface.overlay import Overlay
from src.tools.observer import Observer
import tkinter as tk
from PIL import Image,ImageTk
from threading import RLock
import win32gui

class DofusOverlay(Overlay,Observer):
    def __init__(self,config,order,order_name,mode):
        Overlay.__init__(self)
        Observer.__init__(self,["add_select"])
        self.bind("<<Destroy>>", lambda e: self.destroy())
        self.img = config['img']
        self.perso = dict()
        self.curr_order = []
        self.lock = RLock()
        self.order = []
        self.console = None
        self.selected = order
        
        #perso
        self.frame_perso = tk.Frame(self)
        self.frame_perso.pack(side="left",padx=0, pady=0,fill="both",expand=True)
        
        self.curr_mode = mode
        self.curr_hwnd = 0
        
        self.update_order(order,order_name)
        
        #mode
        frame_mode = tk.Frame(self)
        frame_mode.pack(side="left",padx=0, pady=0,fill="both",expand=True)
        
        img = ImageTk.PhotoImage(Image.open("ressources\\img\\combat.png").resize((30,30)))
        f = tk.Label(frame_mode,image=img)
        f.image = img
        f.pack(side="top",padx=5, pady=5)
        self.combat = f
        
        img = ImageTk.PhotoImage(Image.open("ressources\\img\\hors_combat.jpg").resize((30,30)))
        f = tk.Label(frame_mode,image=img)
        f.image = img
        f.pack(side="top",padx=5, pady=5)
        self.hors_combat = f
        
        self.update_mode(mode)
        
    def alert(self):
        messagebox.showerror(title="Maison", message="Maison en vente !")
        
    def stop(self):
        self.event_generate("<<Destroy>>", when="tail")
            
    def update_perso(self,hwnd):
        self.lock.acquire()
        for h in self.perso:
            if(h==hwnd):
                self.perso[h].config(borderwidth=3, relief="solid")
            else:
                self.perso[h].config(borderwidth=3, relief="flat")
        self.update()
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
        self.update()
        self.curr_mode = mode
        self.lock.release()

    def update_order(self,order,order_name):
        self.lock.acquire()
        if(self.order == order_name):
            self.lock.release()
            return
        self.order = order_name
        self.perso = dict()
        lorder = len(order)
        l = lorder * 94 + 50
        h = 94
        self.geometry(str(l)+"x"+str(h))
        
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
            f = tk.Frame(self.frame_perso,bg="white")
            f.pack(side="left",padx=5, pady=5,fil="both",expand=True)
            l = tk.Label(f,image=img)
            l.bind("<Button-1>", lambda e,hid=hwnd : self.select(hid))
            l.image = img
            l.pack(expand=True)
            self.perso[hwnd] = f
        
        self.update_seleted()
        self.update_perso(self.curr_hwnd)
        self.update()
        self.lock.release()
        
    def new_select_list(self,hwnds):
        self.selected = hwnds
        self.update_seleted()
            
    def select(self,hwnd):
        self.notify("add_select",hwnd)
        win32gui.SetForegroundWindow(self.curr_hwnd)
        
    def close_console(self):
        self.console = None
        
    def open_console(self,cmdobject):
        if(self.console is None):
            self.console = CommandInterface(self,cmdobject)
            self.console.add_observer("destroy",self.close_console)
        self.console.deiconify()
        self.console.entry.focus_set()
        
    def update_seleted(self):
        self.lock.acquire()
        for hwnd in self.perso.keys():
            if(hwnd in self.selected):
                self.perso[hwnd].config(bg="dark sea green")
            else:
                self.perso[hwnd].config(bg="white")
        self.lock.release()
        