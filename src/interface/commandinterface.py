from tkinter import *
from src.tools.observer import Observer

class CommandInterface(Toplevel,Observer):
    def __init__(self, master, cmdobject):
        Toplevel.__init__(self, master)
        Observer.__init__(self,["destroy"])
        self.cmdobject = cmdobject
        self.title("Command")
        self.wm_resizable(False, False)
        self.create_widgets()
        self.bind('<Return>', lambda e : self.cmd())
        self.bind("<Button-1>", lambda e : self.set_focus())
        self.bind("<Up>", lambda e : self.history(e))
        self.bind("<Down>", lambda e : self.history(e))
        self.i = 0
        
    def history(self,event):
        if(len(self.cmdobject.history) > 0):
            if(event.keysym == "Up" and self.i > -1*len(self.cmdobject.history)):
                self.i = (self.i-1)
            elif(event.keysym == "Down" and self.i < 0):
                self.i = (self.i+1)
            
            if(self.i == 0):
                self.textvar.set("")
            else:
                self.textvar.set(self.cmdobject.history[self.i])
            self.entry.icursor(END)
        
    def set_focus(self):
        self.entry.focus_set()

    def create_widgets(self):
        self.main = Frame(self)
        self.text = Text(self.main, bg='black',fg='white',font=('Consolas', 12), state = "normal",height=20, width=90)
        self.scrollbar = Scrollbar(self.main, orient='vertical', command=self.text.yview)
        self.text.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.pack(side="right",fill="y")
        self.text.pack(side="top",fill="both",expand=True)
    
        self.textvar = StringVar()
        self.textvar.trace_add("write", self.reset_i)
        self.entry = Entry(self.main, textvariable=self.textvar, bg='black',fg='white',font=('Consolas', 12), insertbackground='white')
        self.entry.pack(side="bottom",fill="x",pady=("3","0"))
        
        self.main.pack(fill="both",expand=True)
        self.text.config(state = "disabled")
        
    def reset_i(self,a,b,c):
        if(self.textvar.get() == ""):
            self.i = 0
    
    def cmd(self):
        self.text.config(state = "normal")
        inp = self.textvar.get()
        self.textvar.set("")
        self.text.insert(END,f">> {inp}\n")
        rep = self.cmdobject.execute(inp).strip("\n")
        self.text.insert(END,f"{rep}\n")
        self.text.see(END)
        self.text.config(state = "disabled")
        
    def destroy(self):
        super().destroy()
        self.notify("destroy")
        