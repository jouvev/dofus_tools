from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class ChoseInterface(Tk):
    def __init__(self,values,imgsPath,valid_callback):
        Tk.__init__(self)
        self.geometry("800x600")
        self.imgsPath = imgsPath
        self.i = 0
        self.imgFrame = Label(self)
        self.imgFrame.pack(side=TOP,fill=BOTH,expand=True)
        self.show_img(self.imgsPath[self.i])

        framechose = Frame(self, width=500, height=500, bg='white')
        framechose.pack(side=BOTTOM,fill=X,pady=5)

        self.current_var = StringVar()
        combobox = ttk.Combobox(framechose, textvariable=self.current_var,state='readonly')
        combobox['values'] = values

        buttonValid = Button(framechose, text="Valider", command = lambda : valid_callback(self))
        butttonSuivant = Button(framechose, text="Suivant", command=self.next_img)
        butttonPred = Button(framechose, text="Précedent", command=self.pred_img)
        
        butttonPred.pack(side=LEFT,padx=2)
        combobox.pack(side=LEFT,fill=X,expand=True,padx=2)
        buttonValid.pack(side=LEFT,padx=2)
        butttonSuivant.pack(side=LEFT,padx=2)
        
    def set_i(self,i):
        self.i = i
        self.show_img(self.imgsPath[self.i])
        
    def show_img(self,imgpath):
        img = Image.open(imgpath)
        w = img.width
        h = img.height
        if(w>500 or h>500):
            scale = h/w
            if(w>h):
                w = 500
                h = int(w*scale)
            else:
                h = 500
                w = int(h/scale)
        img = img.resize((w,h))
        img = ImageTk.PhotoImage(img)
        self.imgFrame.configure(image=img)
        self.imgFrame.image = img
        
    def pred_img(self):
        if(self.i>0):
            self.i -= 1
            self.show_img(self.imgsPath[self.i])
            
    def get_value(self):
        return self.current_var.get()
    
    def get_img_path(self):
        return self.imgsPath[self.i]
        
    def next_img(self):
        if(self.i<len(self.imgsPath)-1):
            self.i += 1
            self.show_img(self.imgsPath[self.i])
            
