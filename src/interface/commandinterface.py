from tkinter import *

class CommandInterface(Toplevel):
    def __init__(self, master, cmdobject):
        Toplevel.__init__(self, master)
        self.cmdobject = cmdobject
        self.title("Command")
        self.geometry("700x400")
        self.wm_resizable(False, False)
        self.create_widgets()
        self.bind('<Return>', lambda e : self.cmd())

    def create_widgets(self):
        self.text = Text(self,bg='black',fg='white',font=('Consolas', 12))
        self.text.insert(END,">> ")
        self.scrollbar = Scrollbar(self.text, orient='vertical')
        self.scrollbar.pack(side="right", fill ="y")
        self.text.config(borderwidth=2, relief="flat")
        self.text.pack(side="top",fill="both",expand=True,padx=5, pady=5)
        
    def cmd(self):
        inp = self.text.get("1.0",END).split("\n")[-3][2:].strip()
        rep = self.cmdobject.execute(inp).strip("\n")
        self.text.insert(END,f"{rep}\n>> ")