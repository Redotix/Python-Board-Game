import turtle as t
from tkinter import *

win = t.Screen()
win.setup(600, 600)
win.bgcolor("grey")
t.colormode(255)

canvas = win.getcanvas()

menufont = ('Arial', 15, 'normal')


def exitgame():
    exit()


class Mainmenu:
    start = None
    leave = None

    def __init__(self):
        self.start = Button(canvas.master, text="Start Game", command=lambda: self.startbtn(), font=menufont)
        self.leave = Button(canvas.master, text="Exit Game", command=lambda: exitgame(), font=menufont)

    def showmainmenu(self):
        self.start.place(relx=0.5, rely=0.42, anchor=CENTER)
        self.leave.place(relx=0.5, rely=0.58, anchor=CENTER)

    def hidemainmenu(self):
        self.start.place_forget()
        self.leave.place_forget()

    def startbtn(self):
        self.hidemainmenu()
        GameOptions().showgameoptions()


class GameOptions:
    playeramount = 2
    pieceamount = 1
    extratiles = 0

    toptext = None
    playeramountlabel = None
    playeramounthigher = None
    playeramountnumber = None
    playeramountlower = None
    back = None

    def __init__(self):
        self.toptext = Label(canvas.master, text="Choose Game settings", font=menufont)

        self.playeramountlabel = Label(canvas.master, text="Amount of players:", font=menufont)
        self.playeramounthigher = Button(canvas.master, text=">",
                                         command=lambda: self.increaseplayeramount(), font=menufont)

        self.playeramountnumber = Label(canvas.master, text=str(self.playeramount), font=menufont)
        self.playeramountlower = Button(canvas.master, text="<",
                                        command=lambda: self.decreaseplayeramounr(), font=menufont)

        self.back = Button(canvas.master, text="Back", command=lambda: self.backbtn(), font=menufont)

    def showgameoptions(self):
        self.toptext.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.playeramountlabel.place(relx=0.5, rely=0.36, anchor=CENTER)
        self.playeramounthigher.place(relx=0.6, rely=0.42, anchor=CENTER)
        self.playeramountnumber.place(relx=0.5, rely=0.42, anchor=CENTER)
        self.playeramountlower.place(relx=0.4, rely=0.42, anchor=CENTER)

        self.back.place(relx=0.3, rely=0.8, anchor=CENTER)

    def hidegameoptions(self):
        self.toptext.place_forget()

        self.playeramountlabel.place_forget()
        self.playeramounthigher.place_forget()
        self.playeramountnumber.place_forget()
        self.playeramountlower.place_forget()

        self.back.place_forget()

    def increaseplayeramount(self):
        if self.playeramount + 1 <= 4:
            self.playeramount += 1
            self.playeramountnumber.config(text=str(self.playeramount))

    def decreaseplayeramounr(self):
        if self.playeramount - 1 >= 2:
            self.playeramount -= 1
            self.playeramountnumber.config(text=str(self.playeramount))

    def backbtn(self):
        self.hidegameoptions()
        Mainmenu().showmainmenu()


Mainmenu().showmainmenu()

mainloop()
