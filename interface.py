import tkinter as tk
from interfaceframes import *
from interfacecanvas import *

class MainInterface(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, parent)
        self.altnum = tk.IntVar()
        self.parent = parent
        self.parent.minsize(width = 1440, height = 960)
        self.parent.maxsize(width = 1440, height = 960)
        self.GUI(), self.Topcanv(), self.Side1frm(), self.Side2frm(), self.Side3frm()
        
    #Main frames
    def GUI(self):
        self.topbar = Interframes(self.parent,1,"raised","top","both")
        self.sidebar = Interframes(self.parent,0,"flat","left","y")
        self.mainbody = Interframes(self.parent,0,"flat","right","y")

    def Topcanv(self):
        topcanvas = Canvas(self.topbar.frame,1100,175)
        topcanvas.imagecreation(720,90,"topbackground2.png")
        
    #Frames within sidebar
    def Side1frm(self):
        frstfrm = Interframes(self.sidebar.frame,1,"raised","top","x")
        frstbut = Buttons(frstfrm.frame,"settingbutton.png",300,260,"flat",self.Settingsinterface,"normal")

    def Side2frm(self):
        sndfrm = Interframes(self.sidebar.frame,1,"raised","top","x")
        sndbut = Buttons(sndfrm.frame,"writebutton.png",300,260,"flat",self.Writeinterface,"normal")

    def Side3frm(self):
        trdfrm = Interframes(self.sidebar.frame,1,"raised","top","x")
        trdbut = Buttons(trdfrm.frame,"editbutton.png",300,260,"flat",self.Editdatainterface,"normal")

    #Canvas for stuff
    def Maincanv(self):
        self.maincanvas = Canvas(self.mainbody.frame,1000,785)

    def Cleartop(self):
        self.topbar.pack_forget()
        self.topbar = Interframes(self.parent,1,"raised","top","x")

    #Switching the mainbody gui when clicking buttons
    def Switchmid(self):
        if self.altnum == 0:
            self.sidebar.selfdelete()
            self.sidebar = Interframes(self.parent,0,"flat","left","y")
            frstfrm = Interframes(self.sidebar.frame,0,"raised","top","x")
            frstbut = Buttons(frstfrm.frame,"settingbutton.png",300,260,"flat",self.Settingsinterface,"disabled")
            self.Side2frm(), self.Side3frm()
        elif self.altnum == 1:
            self.sidebar.selfdelete()
            self.sidebar = Interframes(self.parent,0,"flat","left","y")
            self.Side1frm()
            sndfrm = Interframes(self.sidebar.frame,0,"raised","top","x")
            sndbut = Buttons(sndfrm.frame,"writebutton.png",300,260,"flat",self.Writeinterface,"disabled")
            self.Side3frm()
        elif self.altnum == 2:
            self.mainbody.selfdelete()
            self.sidebar.selfdelete()
            self.sidebar = Interframes(self.parent,0,"flat","left","y")
            self.mainbody = Interframes(self.parent,0,"flat","right","y")
            self.Side1frm(),self.Side2frm()
            trdfrm = Interframes(self.sidebar.frame,0,"raised","top","x")
            trdbut = Buttons(trdfrm.frame,"editbutton.png",300,260,"flat",self.Editdatainterface,"disabled")
            tablefrm = Interframes(self.mainbody.frame,0,"raised","top","both")
            self.table = Tableviewer(tablefrm)
        else:
            pass

    def Settingsinterface(self):
        if self.altnum == 0:
            pass
        if self.altnum == 2:
            self.mainbody.selfdelete()
        self.altnum = 0
        self.Switchmid()
        #self. something

    def Writeinterface(self):
        #Check to see if writing is done.
        if self.altnum == 1:
            pass
        elif self.altnum == 2:
            self.mainbody.selfdelete()
        self.altnum = 1
        self.Switchmid()
        #self something
        
    def Editdatainterface(self):
        if self.altnum == 2:
            self.table.selfdelete()
        self.altnum = 2
        self.Switchmid()
        self.editdatafrm = Interframes(self.mainbody.frame,1,"raised","bottom","x")
        editcanvas = Canvas(self.editdatafrm.frame,1000,200)
        editcanvas.imagecreation(500,100,"editbackground.png")
        editcanvas.editcanvas()
        
        


if __name__ == "__main__":
    root = tk.Tk()
    MainInterface(root).pack(side="top", fill="both", expand = True)
    root.mainloop()

