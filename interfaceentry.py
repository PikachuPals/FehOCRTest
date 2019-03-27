import tkinter as tk

class Entrybox(tk.Entry):
    def __init__(self,parent,txt):
        tk.Entry.__init__(self, parent)
        self.parent = parent
        self.txt = txt
        self.entry = tk.Entry(master = self.parent)
        self.entry.pack()
        self.entry.insert(0, self.txt)
        self.entry.bind('<FocusIn>', self.click)
        self.entry.bind('<FocusOut>', self.notfocus)
        self.entry.config(fg = "grey")

    def getvalue(self):
        self.item = self.entry.get()
        return self.item

    def click(self, event):
        if self.getvalue() == self.txt:
            self.entry.delete(0,"end")
            self.entry.insert(0, "")
            self.entry.config(fg = "black")

    def notfocus(self, event):
        if self.getvalue() == "":
            self.entry.insert(0, self.txt)
            self.entry.config(fg = "grey")
