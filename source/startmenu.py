from tkinter import *
from inputs import *

canvas = win.getcanvas()

menufont = ('Arial', 15, 'normal')


def exitgame():
    exit()


class Mainmenu:
    start = None
    leave = None
    gameguide = None
    gamename = None

    def __init__(self):
        self.start = Button(canvas.master, text="Start Game", command=lambda: self.startbtn(), font=menufont)
        self.leave = Button(canvas.master, text="Exit Game", command=lambda: exitgame(), font=menufont)
        self.gameguide = Button(canvas.master, text="Game Guide", command=lambda: self.gameguidebtn(), font=menufont)
        self.gamename = Label(text="Game Name", font=menufont)

    def showmainmenu(self):
        self.start.place(relx=0.5, rely=0.42, anchor=CENTER)
        self.leave.place(relx=0.5, rely=0.58, anchor=CENTER)
        self.gameguide.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.gamename.place(relx=0.5, rely=0.3, anchor=CENTER)

    def hidemainmenu(self):
        self.start.place_forget()
        self.leave.place_forget()
        self.gameguide.place_forget()
        self.gamename.place_forget()

    def startbtn(self):
        self.hidemainmenu()
        GameOptions().showgameoptions()

    def gameguidebtn(self):
        self.hidemainmenu()
        GameGuide().showgameguide()


class GameOptions:
    playeramount = 2
    pieceamount = 1
    tileamount = 0

    toptext = None
    playeramountlabel = None
    playeramounthigher = None
    playeramountnumber = None
    playeramountlower = None

    pieceamountlabel = None
    pieceamounthigher = None
    pieceamountnumber = None
    pieceamountlower = None

    tileamountlabel = None
    tileamounthigher = None
    tileamountnumber = None
    tileamountlower = None
    back = None
    startgame = None

    def __init__(self):
        self.toptext = Label(canvas.master, text="Choose Game settings", font=menufont)

        # Player amount widgets
        self.playeramountlabel = Label(canvas.master, text="Amount of players:", font=menufont)
        self.playeramounthigher = Button(canvas.master, text=">",
                                         command=lambda: self.increaseplayeramount(), font=menufont)

        self.playeramountnumber = Label(canvas.master, text=str(self.playeramount), font=menufont)
        self.playeramountlower = Button(canvas.master, text="<",
                                        command=lambda: self.decreaseplayeramount(), font=menufont)

        # Piece amount widgets
        self.pieceamountlabel = Label(canvas.master, text="Amount of pieces:", font=menufont)
        self.pieceamounthigher = Button(canvas.master, text=">",
                                        command=lambda: self.increasepieceamount(), font=menufont)

        self.pieceamountnumber = Label(canvas.master, text=str(self.pieceamount), font=menufont)
        self.pieceamountlower = Button(canvas.master, text="<",
                                       command=lambda: self.decreasepieceamount(), font=menufont)

        # Tile amount widgets
        self.tileamountlabel = Label(canvas.master, text="Amount of extra tiles:", font=menufont)
        self.tileamounthigher = Button(canvas.master, text=">",
                                       command=lambda: self.increasetileamount(), font=menufont)

        self.tileamountnumber = Label(canvas.master, text=str(self.tileamount), font=menufont)
        self.tileamountlower = Button(canvas.master, text="<",
                                      command=lambda: self.decreasetileamount(), font=menufont)

        self.back = Button(canvas.master, text="Back", command=lambda: self.backbtn(), font=menufont)
        self.startgame = Button(canvas.master, text="Start", command=lambda: self.startbtn(), font=menufont)

    def showgameoptions(self):
        self.toptext.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.playeramountlabel.place(relx=0.5, rely=0.36, anchor=CENTER)
        self.playeramounthigher.place(relx=0.6, rely=0.42, anchor=CENTER)
        self.playeramountnumber.place(relx=0.5, rely=0.42, anchor=CENTER)
        self.playeramountlower.place(relx=0.4, rely=0.42, anchor=CENTER)

        self.pieceamountlabel.place(relx=0.5, rely=0.48, anchor=CENTER)
        self.pieceamounthigher.place(relx=0.6, rely=0.54, anchor=CENTER)
        self.pieceamountnumber.place(relx=0.5, rely=0.54, anchor=CENTER)
        self.pieceamountlower.place(relx=0.4, rely=0.54, anchor=CENTER)

        self.tileamountlabel.place(relx=0.5, rely=0.60, anchor=CENTER)
        self.tileamounthigher.place(relx=0.6, rely=0.66, anchor=CENTER)
        self.tileamountnumber.place(relx=0.5, rely=0.66, anchor=CENTER)
        self.tileamountlower.place(relx=0.4, rely=0.66, anchor=CENTER)

        self.back.place(relx=0.3, rely=0.8, anchor=CENTER)
        self.startgame.place(relx=0.7, rely=0.8, anchor=CENTER)

    def hidegameoptions(self):
        self.toptext.place_forget()

        self.playeramountlabel.place_forget()
        self.playeramounthigher.place_forget()
        self.playeramountnumber.place_forget()
        self.playeramountlower.place_forget()

        self.pieceamountlabel.place_forget()
        self.pieceamounthigher.place_forget()
        self.pieceamountnumber.place_forget()
        self.pieceamountlower.place_forget()

        self.tileamountlabel.place_forget()
        self.tileamounthigher.place_forget()
        self.tileamountnumber.place_forget()
        self.tileamountlower.place_forget()

        self.back.place_forget()
        self.startgame.place_forget()

    def increaseplayeramount(self):
        if self.playeramount + 1 <= 4:
            self.playeramount += 1
            self.playeramountnumber.config(text=str(self.playeramount))

    def decreaseplayeramount(self):
        if self.playeramount - 1 >= 2:
            self.playeramount -= 1
            self.playeramountnumber.config(text=str(self.playeramount))

    def increasepieceamount(self):
        if self.pieceamount + 1 <= 11 and self.pieceamount + 1 <= self.tileamount + 1:
            self.pieceamount += 1
            self.pieceamountnumber.config(text=str(self.pieceamount))

    def decreasepieceamount(self):
        if self.pieceamount - 1 >= 1:
            self.pieceamount -= 1
            self.pieceamountnumber.config(text=str(self.pieceamount))

    def increasetileamount(self):
        if self.tileamount + 1 <= 10:
            self.tileamount += 1
            self.tileamountnumber.config(text=str(self.tileamount))

    def decreasetileamount(self):
        if self.tileamount - 1 >= 0:
            self.tileamount -= 1
            self.tileamountnumber.config(text=str(self.tileamount))
            if self.tileamount < self.pieceamount - 1:
                self.pieceamount -= 1
                self.pieceamountnumber.config(text=str(self.pieceamount))

    def backbtn(self):
        self.hidegameoptions()
        Mainmenu().showmainmenu()

    def startbtn(self):
        self.hidegameoptions()
        GameMaster(self.playeramount, self.pieceamount, self.tileamount)
        GameMaster.inmenu = False


class GameGuide:
    back = None

    def __init__(self):
        self.back = Button(canvas.master, text="Back", command=lambda: self.backbtn(), font=menufont)

    def showgameguide(self):
        self.back.place(relx=0.3, rely=0.8, anchor=CENTER)

    def hidegameguide(self):
        self.back.place_forget()

    def backbtn(self):
        self.hidegameguide()
        Mainmenu().showmainmenu()


Mainmenu().showmainmenu()

win.mainloop()
