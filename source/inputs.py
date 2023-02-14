from gamemaster import *
from tkinter import *


class InputSystem:
    gamefont = ('Arial', int(windowsize / fontsizefactor), 'normal')

    master = None
    # master = GameMaster(4, 4, 3)
    # master.inmenu = False

    def __init__(self):
        win.onkey(lambda key="Return": self.inputhandler(key), "Return")
        win.onkey(lambda key="Space": self.inputhandler(key), "space")
        win.onkey(lambda key="Left": self.inputhandler(key), "Left")
        win.onkey(lambda key="Right": self.inputhandler(key), "Right")
        rollbtn = Button(canvas.master, text="Roll", command=lambda key="Space": self.inputhandler(key),
                         font=self.gamefont)
        movebtn = Button(canvas.master, text="Move", command=lambda key="Return": self.inputhandler(key),
                         font=self.gamefont)
        rollbtn.place(relx=0.7, rely=0.05, anchor=CENTER)
        movebtn.place(relx=0.3, rely=0.05, anchor=CENTER)

        win.onclick(self.mouseselectpiece)

        win.listen()

    def mouseselectpiece(self, x, y):
        position = (int(x), int(y))

        piecelist = self.master.players[self.master.playerchoice].playerPieces
        for pi in range(len(piecelist)):
            if position == piecelist[pi].position:
                self.master.piecechoice = pi
                Renderer().highlight((position[0] + 0.5, position[1] + 0.5))
                Renderer().refreshui(self.master.playingfield.canvassize[1],
                                     self.master.settings.playernames[self.master.playerchoice],
                                     self.master.piecechoice, self.master.roll, self.gamefont[1],
                                     self.master.settings.playernames)
                return

    def cyclepiecesright(self):
        if self.master.piecechoice + 1 > self.master.settings.pieceamount - 1:
            self.master.piecechoice = 0
        else:
            self.master.piecechoice += 1

        pos = self.master.players[self.master.playerchoice].playerPieces[self.master.piecechoice].position
        Renderer().highlight((pos[0] + 0.5, pos[1] + 0.5))
        print(self.master.piecechoice)

    def cyclepiecesleft(self):
        if self.master.piecechoice - 1 < 0:
            self.master.piecechoice = self.master.settings.pieceamount - 1
        else:
            self.master.piecechoice -= 1

        pos = self.master.players[self.master.playerchoice].playerPieces[self.master.piecechoice].position
        Renderer().highlight((pos[0] + 0.5, pos[1] + 0.5))
        print(self.master.piecechoice)

    def roll(self):
        if self.master.roll == 0:
            # self.master.roll = random.randrange(1, 7)
            self.master.roll = 6

    def cycleplayers(self):
        if self.master.playerchoice + 1 > self.master.settings.playeramount - 1:
            self.master.playerchoice = 0
        else:
            self.master.playerchoice += 1

        pos = self.master.players[self.master.playerchoice].playerPieces[self.master.piecechoice].position
        Renderer().highlight((pos[0] + 0.5, pos[1] + 0.5))

    def inputhandler(self, key):
        if self.master.inmenu is False:
            match key:
                case "Left":
                    self.cyclepiecesleft()
                case "Right":
                    self.cyclepiecesright()
                case "Return":
                    self.moveattempt()
                case "Space":
                    self.roll()

            Renderer().refreshui(self.master.playingfield.canvassize[1],
                                 self.master.settings.playernames[self.master.playerchoice],
                                 self.master.piecechoice, self.master.roll, self.gamefont[1],
                                 self.master.settings.playernames)

    def moveattempt(self):
        if self.master.roll != 0:
            piecesonboard = None

            piece = self.master.players[self.master.playerchoice].playerPieces[self.master.piecechoice]

            for i in range(len(self.master.players[self.master.playerchoice].playerPieces)):
                if self.master.players[self.master.playerchoice].playerPieces[i].positioninplayingfield is not None:
                    piecesonboard = True
                elif piecesonboard is not True:
                    piecesonboard = False

            print("piece on board is ", piecesonboard)

            if piecesonboard is False and self.master.roll == 6:
                self.master.initiatepiece()
                self.cycleplayers()
                self.master.roll = 0
                self.master.attempt = 0
                print("Placed piece of playing field")
                return

            elif piecesonboard is False and self.master.roll != 6:
                if self.master.attempt + 1 > 2:
                    self.master.roll = 0
                    self.master.attempt = 0
                    self.cycleplayers()
                    print("Out of attempts, turn skipped")
                else:
                    self.master.roll = 0
                    self.master.attempt += 1
                    print("Didnt throw 6, you have another attempt")
                return

            if piece.positioninplayingfield is None and self.master.roll == 6:
                self.master.initiatepiece()
                self.cycleplayers()
                self.master.roll = 0
                print("Placed piece of playing field")
                return

            elif piece.positioninplayingfield is None and self.master.roll != 6:
                print("Didnt roll a 6, choose a different piece or skip turn")
                return

            if self.master.performmovement(self.master.roll) is True:
                self.cycleplayers()
                self.master.roll = 0
                print("Moved piece")
                return
            if self.master.performmovement(self.master.roll) is False:
                print("Piece cant move there, choose a different piece or skip turn")
                return
            print("something went wrong")


# inputsystem = InputSystem()
# win.mainloop()
