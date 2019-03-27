import tkinter as tk
from PIL import Image
from PIL import ImageTk as itk
from tableviewer import *
import interface as inter

class Buttons(tk.Button):
    
    def __init__(self,parent,im,w,h,rlf,cmd,st):
        tk.Button.__init__(self)
        self.img = Image.open(im)
        self.img1 = itk.PhotoImage(self.img)
        self.button = tk.Button(master = parent, width = w, height = h,relief = rlf,overrelief = "groove",image = self.img1,command = cmd,state = st)
        self.button.image = self.img1
        self.button.pack(side = "top",pady = 1, padx = 0)

