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

    def create_widgets(self):
        self.main = Frame(self)
        self.text = Text(self.main, bg='black',fg='white',font=('Consolas', 12), state = "normal",height=20, width=90)
        self.scrollbar = Scrollbar(self.main, orient='vertical', command=self.text.yview)
        self.text.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.pack(side="right",fill="y")
        self.text.pack(side="top",fill="both",expand=True)
    
        self.textvar = StringVar()
        self.entry = Entry(self.main, textvariable=self.textvar, bg='black',fg='white',font=('Consolas', 12), insertbackground='white')
        self.entry.pack(side="bottom",fill="x",pady=("3","0"))
        
        self.main.pack(fill="both",expand=True)
        self.text.config(state = "disabled")
    
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
        