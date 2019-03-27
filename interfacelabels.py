import tkinter as tk
from PIL import Image
from PIL import ImageTk as itk

class Labels(tk.Label):

    def __init__(self,parent,curs,hlbg,hlc,im,rl,st):
        tk.Label.__init__(self)
        self.parent = parent
        self.img = Image.open(im)
        self.img1 = itk.PhotoImage(self.img)
        self.label = tk.Label(master = self.parent ,cursor = curs, highlightbackground = hlbg, highlightcolor = hlc, image = self.img1, relief = rl, state = st)
        self.label.image = self.img1
        
