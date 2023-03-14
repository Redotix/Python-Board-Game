from gamemaster import *
from tkinter import *


class InputSystem:
    rollbtn = None
    movebtn = None
    resultscreen = None

    master = None
    # master = GameMaster(4, 4, 3)
    # master.inmenu = False

    def __init__(self, resultscreen):
        win.onkey(lambda key="Return": self.inputhandler(key), "Return")
        win.onkey(lambda key="Space": self.inputhandler(key), "space")
        win.onkey(lambda key="Left": self.inputhandler(key), "Left")
        win.onkey(lambda key="Right": self.inputhandler(key), "Right")
        self.rollbtn = Button(canvas.master, text="Hoď", command=lambda key="Space": self.inputhandler(key), font=gamefont)
        self.movebtn = Button(canvas.master, text="Choď", command=lambda key="Return": self.inputhandler(key), font=gamefont)
        self.rollbtn.place(relx=0.7, rely=0.05, anchor=CENTER)
        self.movebtn.place(relx=0.3, rely=0.05, anchor=CENTER)
        self.resultscreen = resultscreen

        win.onclick(self.mouseselectpiece)

        win.listen()

    def inputhandler(self, key):
        if self.master.inmenu is False and self.master.currentGameState != GAMESTATE_AWAIT:
            match key:
                case "Left":
                    self.cyclepiecesleft()
                case "Right":
                    self.cyclepiecesright()
                case "Return":
                    if self.master.roll == 0:
                        return

                    self.moveattempt(self.master.players[self.master.playerchoice].playerPieces[self.master.piecechoice])
                case "Space":
                    self.roll()
                    if self.master.currentGameState == GAMESTATE_GETPIECEOUT:
                        self.moveattempt(self.master.players[self.master.playerchoice].playerPieces[self.master.piecechoice])

        self.master.refreshui()

    def mouseselectpiece(self, x, y):
        position = (int(x), int(y))

        piecelist = self.master.players[self.master.playerchoice].playerPieces
        for pi in range(len(piecelist)):
            if position == piecelist[pi].position:
                self.master.piecechoice = pi
                Renderer().highlight((position[0] + 0.5, position[1] + 0.5))
                self.master.refreshui()
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
        if self.master.currentGameState != GAMESTATE_MOVE:
            self.master.roll = random.randrange(1, 7)
            self.master.refreshui()

        if self.master.currentGameState != GAMESTATE_GETPIECEOUT:
            self.master.currentGameState = GAMESTATE_MOVE

    def debugroll(self, roll):
        if self.master.currentGameState != GAMESTATE_MOVE:
            self.master.roll = roll
            self.master.refreshui()

        if self.master.currentGameState != GAMESTATE_GETPIECEOUT:
            self.master.currentGameState = GAMESTATE_MOVE

    def gotoresultscreen(self, victor):
        recreatescreen()
        resetstate()
        self.movebtn.place_forget()
        self.rollbtn.place_forget()
        self.resultscreen.victor = victor
        self.resultscreen.showresultscreen()

    def cycleplayers(self):
        haswinner = True
        player = self.master.players[self.master.playerchoice]
        for i in player.playerPieces:
            if i.isinhouse is False:
                haswinner = False
                break

        if haswinner is True:
            print(f' {self.master.settings.playernames[self.master.playerchoice]} won!')
            self.gotoresultscreen(self.master.settings.playernames[self.master.playerchoice])

        if self.master.playerchoice + 1 > self.master.settings.playeramount - 1:
            self.master.playerchoice = 0
        else:
            self.master.playerchoice += 1

        if self.ispieceonboard():
            self.master.currentGameState = GAMESTATE_ROLL
        else:
            self.master.currentGameState = GAMESTATE_GETPIECEOUT

        self.master.roll = 0
        self.master.attempt = 0

        pos = self.master.players[self.master.playerchoice].playerPieces[self.master.piecechoice].position
        Renderer().highlight((pos[0] + 0.5, pos[1] + 0.5))

    def ispieceonboard(self):
        for i in range(len(self.master.players[self.master.playerchoice].playerPieces)):
            if self.master.players[self.master.playerchoice].playerPieces[i].positioninplayingfield is not None:
                return True

        return False

    def canpiecemove(self, roll, piece):
        if piece.positioninplayingfield is None:
            return False
        if self.master.lenghtoftravel - piece.tilesmoved > roll and piece.positioninhouse == -1:
            print(f'PIECE CAN STILL TRAVEL ON FIELD {self.master.lenghtoftravel - piece.tilesmoved} GREATER THAN {roll}')
            return True
        if piece.positioninhouse + roll < self.master.settings.pieceamount:
            print(f'PIECE CAN STILL TRAVEL IN HOUSES {piece.positioninhouse + roll} LESS THAN {self.master.settings.pieceamount}')
            return True
        if piece.tilesmoved + roll + piece.positioninhouse <= self.master.lenghtoftravel - 1 + self.master.settings.pieceamount:
            return True

        return False
    
    def cananypiecemove(self, roll):
        availablemoves = 0

        for i in range(len(self.master.players[self.master.playerchoice].playerPieces)):
            piece = self.master.players[self.master.playerchoice].playerPieces[i]

            if piece.positioninplayingfield is None and roll == 6 or self.canpiecemove(roll, piece):
                availablemoves += 1

        return availablemoves

    def moveattempt(self, piece):
        if self.master.currentGameState == GAMESTATE_GETPIECEOUT:
            if self.master.roll == 6:
                self.master.initiatepiece()
                self.cycleplayers()
                self.master.statetext = ""

            elif self.master.attempt + 1 > 2:
                self.cycleplayers()
                self.master.statetext = "Došli ti pokusi"
            else:
                self.master.attempt += 1
                self.master.statetext = "Máš dalšlí pokus"
            return

        elif piece.positioninplayingfield is None and self.master.currentGameState == GAMESTATE_MOVE:
            if self.master.roll == 6:
                if self.master.initiatepiece():
                    self.cycleplayers()
                    self.master.statetext = ""
                    return
                self.master.currentGameState = GAMESTATE_MOVE
                return
        
        availablemoves = self.cananypiecemove(self.master.roll)
        print(f'Available moves is {availablemoves}')

        if availablemoves <= 0:
            self.cycleplayers()
            self.master.statetext = "0 možných pohybov"
            return

        if not self.canpiecemove(self.master.roll, piece):
            self.master.statetext = "Neplatný pohyb"
            return
        
        result = self.master.performmovement(self.master.roll)
        print(f'Result of move is {result}')

        match result:
            case 0:  # MOVESTATE_SUCCESS
                self.master.statetext = ""
                self.cycleplayers()
            case 1:  # MOVESTATE_OUTOFBOUNDS
                if availablemoves <= 1:
                    self.master.statetext = "Neplatný pohyb, 0 možných pohybov"
                    self.cycleplayers()
                    return
                self.master.statetext = "Neplatný pohyb"
                self.master.currentGameState = GAMESTATE_MOVE
            case 2:  # MOVESTATE_TILEOCCUPIED
                if availablemoves <= 1:
                    self.master.statetext = "Neplatný pohyb, 0 možných pohybov"
                    self.cycleplayers()
                    return
                self.master.currentGameState = GAMESTATE_MOVE
                self.master.statetext = "Neplatný pohyb"

# inputsystem = InputSystem()
# win.mainloop()
