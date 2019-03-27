import tkinter as tk
import tkinter.font as tkfont
import tkinter.ttk as ttk
import sqlite3
import interface as inter
from database import *

class Tableviewer(object):
    def __init__(self,parent):
        self.tree = None
        self.parent = parent
        self.__labelcreation__()
        self.__treebuild__()

    def __labelcreation__(self):
        self.container = self.parent.frame
        self.container.pack(fill="both",expand=True)
        self.tree = ttk.Treeview(columns=table,show = "headings")
        
        scrolly = ttk.Scrollbar(orient = "vertical", command = self.tree.yview)
        scrollx = ttk.Scrollbar(orient = "horizontal", command = self.tree.xview)
        
        self.tree.configure(yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        self.tree.grid(column = 0, row = 0, sticky = "nsew", in_=self.container)
        scrolly.grid(column = 1,row = 0, sticky = "ns", in_=self.container)
        scrollx.grid(column = 0, row = 1, sticky = "ew", in_=self.container)
        self.container.grid_columnconfigure(0, weight = 1)
        self.container.grid_rowconfigure(0, weight = 1)

    def __treebuild__(self):
        for columns in table:
            self.tree.heading(columns, text = columns.title(),command = lambda c=columns: self.sorting(self.tree, c, 0))
            self.tree.column(columns, width = tkfont.Font().measure(columns.title()))

        for skills in database:
            self.tree.insert("",'end',values=skills)
            for c, value in enumerate(skills):
                col_w = tkfont.Font().measure(value)
                if self.tree.column(table[c], width = None)< col_w:
                    self.tree.column(table[c], width = col_w)

    def sorting(self,tree, col, descend):
        data = [(tree.set(child, col), child) for child in tree.get_children("")]
        data.sort(reverse = descend)
        for c, val in enumerate(data):
            tree.move(val[1],"",c)
        tree.heading(col, command=lambda col=col: self.sorting(tree, col, int(not descend)))

    def selfdelete(self):
        self.container.pack_forget()
        

def fetchdata():
    db_feh = "fehdatabase.db"
    db = connection(db_feh)
    cursor = conncursor(db_feh)
    cursor.execute('SELECT Id, Title,Name,Level,HP,Atk,Spd,Def,Res,SP,Weapon,Assist,Special,SkillA,SkillB,SkillC FROM heroes WHERE Hidden = 0;')
    data = cursor.fetchall()
    return data
    
table = ['Id', 'Title','Name','Level','HP','Atk','Spd','Def','Res','SP','Weapon','Assist','Special','SkillA','SkillB','SkillC']
database = fetchdata()








        
        
        
        
        
        
