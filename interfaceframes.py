import tkinter as tk

class Interframes(tk.Frame):

    def __init__(self,parent,bw,rlf, sd,fil):
        tk.Frame.__init__(self, parent)
        self.frame = tk.Frame(master = parent, background = "gray",bd = bw, relief = rlf)
        self.frame.pack(side = sd,fill = fil)
    
    def selfdelete(self):
        self.frame.pack_forget()
    
