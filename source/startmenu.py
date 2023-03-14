from inputs import *
import sys

menufont = ('Arial', int(windowsize / fontsizefactor), 'normal')
titlefont = ('Comic Sans MS', int(windowsize / (fontsizefactor * 0.5)), 'normal')


def rgbtohex(rgb):
    return "#%02x%02x%02x" % rgb


def exitgame():
    sys.exit(0)


class Mainmenu:
    start = None
    leave = None
    gameguide = None
    gamename = None

    def __init__(self):
        self.start = Button(canvas.master, text="Hrať", width=int(windowsize / 50),
                            command=lambda: self.startbtn(), font=menufont)
        self.leave = Button(canvas.master, text="Koniec", width=int(windowsize / 50),
                            command=lambda: exitgame(), font=menufont)
        self.gameguide = Button(canvas.master, text="Ako hrať", width=int(windowsize / 50),
                                command=lambda: self.gameguidebtn(), font=menufont)
        self.gamename = Label(text="Cloveče Nehnevaj Sa!", font=titlefont, bg=rgbtohex(bgcolor))

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
        options.showgameoptions()

    def gameguidebtn(self):
        self.hidemainmenu()
        guide.showgameguide()


class GameOptions:
    playeramount = 4
    pieceamount = 4
    tileamount = 3

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

    namesbtn = None
    names = ["Modrý", "Žltý", "Zelený", "Červený"]
    entryfields = []

    startgame = None

    inputsystem = None

    def __init__(self):
        self.toptext = Label(canvas.master, text="Zvol nastavenia hry", font=menufont, bg=rgbtohex(bgcolor))

        # Player amount widgets
        self.playeramountlabel = Label(canvas.master, text="Počet hráčov:", font=menufont, bg=rgbtohex(bgcolor))
        self.playeramounthigher = Button(canvas.master, text=">",
                                         command=lambda: self.increaseplayeramount(), font=menufont)

        self.playeramountnumber = Label(canvas.master, text=str(self.playeramount), font=menufont, bg=rgbtohex(bgcolor))
        self.playeramountlower = Button(canvas.master, text="<",
                                        command=lambda: self.decreaseplayeramount(), font=menufont)

        # Piece amount widgets
        self.pieceamountlabel = Label(canvas.master, text="Počet figúrok:", font=menufont, bg=rgbtohex(bgcolor))
        self.pieceamounthigher = Button(canvas.master, text=">",
                                        command=lambda: self.increasepieceamount(), font=menufont)

        self.pieceamountnumber = Label(canvas.master, text=str(self.pieceamount), font=menufont, bg=rgbtohex(bgcolor))
        self.pieceamountlower = Button(canvas.master, text="<",
                                       command=lambda: self.decreasepieceamount(), font=menufont)

        # Tile amount widgets
        self.tileamountlabel = Label(canvas.master, text="Veľkosť hernej plochy:", font=menufont, bg=rgbtohex(bgcolor))
        self.tileamounthigher = Button(canvas.master, text=">",
                                       command=lambda: self.increasetileamount(), font=menufont)

        self.tileamountnumber = Label(canvas.master, text=str(self.tileamount), font=menufont, bg=rgbtohex(bgcolor))
        self.tileamountlower = Button(canvas.master, text="<",
                                      command=lambda: self.decreasetileamount(), font=menufont)

        self.back = Button(canvas.master, text="Späť", command=lambda: self.backbtn(), font=menufont)
        self.namesbtn = Button(canvas.master, text="Zvoľ mená", command=lambda: self.namewindow(), font=menufont)
        self.startgame = Button(canvas.master, text="Hrať", command=lambda: self.startbtn(), font=menufont)

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
        self.namesbtn.place(relx=0.5, rely=0.8, anchor=CENTER)
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
        self.namesbtn.place_forget()
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
        main.showmainmenu()

    def namewindow(self):
        namewindow = Toplevel(canvas)
        namewindow.title("Zvoľ mená")
        namewindowsize = str(int(windowsize / 3)) + "x" + str(int(windowsize / 3))
        namewindow.geometry(str(namewindowsize))
        self.entryfields = []

        def closenamewindow():
            for playernames in range(self.playeramount):
                self.names[playernames] = self.entryfields[playernames].get()
            namewindow.destroy()

        Label(namewindow, text="Zvoľ mená hráčov", font=menufont).pack()
        for players in range(self.playeramount):
            entryfield = Entry(namewindow, font=menufont)
            entryfield.insert(0, self.names[players])
            self.entryfields.append(entryfield)
            self.entryfields[players].pack()

        Button(namewindow, text="Potvrdiť", command=lambda: closenamewindow(), font=menufont).pack()

    def startbtn(self):
        Settings.playernames = ["", "", "", ""]
        for playernames in range(self.playeramount):
            Settings.playernames[playernames] = self.names[playernames]

        self.hidegameoptions()
        self.inputsystem = InputSystem(ResultScreen())
        self.inputsystem.master = GameMaster(self.playeramount, self.pieceamount, self.tileamount)
        GameMaster.inmenu = False


class GameGuide:
    back = None

    def __init__(self):
        self.back = Button(canvas.master, text="Späť", command=lambda: self.backbtn(), font=menufont)

    def showgameguide(self):
        self.back.place(relx=0.3, rely=0.8, anchor=CENTER)

    def hidegameguide(self):
        self.back.place_forget()

    def backbtn(self):
        self.hidegameguide()
        main.showmainmenu()


class ResultScreen:
    title = None
    back = None
    victor = None

    def __init__(self):
        self.title = Label(text="X vyhral!", font=titlefont, bg=rgbtohex(bgcolor))
        self.back = Button(canvas.master, text="Späť do hlavného menu", command=lambda: self.backbtn(), font=menufont)

    def showresultscreen(self):
        self.title.config(text=f'{self.victor} vyhral!')
        self.title.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.back.place(relx=0.5, rely=0.8, anchor=CENTER)

    def hideresultscreen(self):
        self.title.place_forget()
        self.back.place_forget()

    def backbtn(self):
        self.hideresultscreen()
        main.showmainmenu()


main = Mainmenu()
options = GameOptions()
guide = GameGuide()
result = ResultScreen()

Mainmenu().showmainmenu()
win.mainloop()
