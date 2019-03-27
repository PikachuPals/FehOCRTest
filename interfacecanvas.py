import tkinter as tk
from PIL import Image
from PIL import ImageTk as itk
from interfaceentry import *
from interfacebuttons import *
from interfacelabels import *
from interfaceframes import *

class Canvas(tk.Canvas):
    def __init__(self,parent,w,h):
        tk.Canvas.__init__(self,parent)
        self.parent = parent
        self.canvas = tk.Canvas(master = parent,width = w,height = h,bd = 0)
        self.canvas.pack(fill = "both")
        self.occupation = 0

    def imagecreation(self,posx,posy,im):
        img = Image.open(im)
        img1 = itk.PhotoImage(img)
        self.canvas.create_image(posx,posy,image = img1)
        self.canvas.image = img1
        
    def buttonplacement(self, im, cmd):
        self.img = Image.open(im)
        self.img1 = itk.PhotoImage(self.img)
        self.editbutton = tk.Button(master = self.parent, width = 120, height = 40, relief = "flat", overrelief = "groove",image = self.img1, command = cmd,state = "active") 
        self.editbutton.image = self.img1
        self.editbutton_window = self.canvas.create_window(65,25,window = self.editbutton, tags = "clear")

    def entryplacement(self, txt, posx, posy):
        self.txt = txt
        self.entryfrm = tk.Frame(master = self.parent, background = "grey",bd = 0, relief = "flat")
        self.entry = Entrybox(self.entryfrm, self.txt)
        self.entry_window = self.canvas.create_window(posx, posy, window = self.entryfrm, tags = "clear")
        
    def editcanvas(self):
        self.canvas.delete("clear")
        self.buttonplacement("editlabel.png", self.deletecanvas)
        self.entryplacement("Id",210,80)
        self.entryplacement("Skill",540,80)
        self.entryplacement("Value",870,80)        

    def deletecanvas(self):
        self.canvas.delete("clear")
        self.buttonplacement("deletelabel.png", self.recovercanvas)
        self.entryplacement("Id",540,80)

    def recovercanvas(self):
        self.canvas.delete("clear")
        self.buttonplacement("recoverlabel.png", self.editcanvas)
        self.entryplacement("Id",540,80)
        
