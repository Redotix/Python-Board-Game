from Settings import *
from Renderer import *
from PlayField import *
from Player import *
import random

win = t.Screen()
canvas = win.getcanvas()
root = canvas.winfo_toplevel()
root.resizable(False, False)
windowsize = canvas.winfo_screenheight() - 210
win.setup(windowsize, windowsize + 90)
t.colormode(255)
bgcolor = (128, 128, 128)
win.bgcolor(bgcolor)

fontsizefactor = 40
gamefont = ('Arial', int(windowsize / fontsizefactor), 'normal')


def recreatescreen():
    t.Screen().clear()
    t.colormode(255)
    win.bgcolor(bgcolor)


GAMESTATE_AWAIT = -1
GAMESTATE_READY = 0
GAMESTATE_GETPIECEOUT = 1
GAMESTATE_ROLL = 2
GAMESTATE_MOVE = 3

MOVESTATE_SUCCESS = 0
MOVESTATE_OUTOFBOUNDS = 1
MOVESTATE_TILEOCCUPIED = 2


def resetstate():
    GameMaster.settings = None
    GameMaster.playingfield = None

    GameMaster.currentGameState = 1

    GameMaster.lenghtoftravel = 0
    GameMaster.players = []
    GameMaster.playerchoice = 0
    GameMaster.piecechoice = 0
    GameMaster.roll = 0
    GameMaster.attempt = 0
    GameMaster.inmenu = True

    GameMaster.statetext = ""


class GameMaster:
    settings = None
    playingfield = None

    currentGameState = 1

    lenghtoftravel = 0
    players = []
    playerchoice = 0
    piecechoice = 0
    roll = 0
    attempt = 0
    inmenu = True

    statetext = ""

    def __init__(self, playeramount, pieceamount, extratiles):
        t.tracer(False)
        self.settings = Settings(playeramount, pieceamount, extratiles)
        self.playingfield = PlayField()

        self.playingfield.generatefield(self.settings.extratiles, windowsize)
        self.lenghtoftravel = len(self.playingfield.fieldTiles)
        win.setworldcoordinates(
            0, 0, self.playingfield.canvassize[1], self.playingfield.canvassize[0])

        for i in range(len(self.playingfield.decoration)):
            Renderer().render((102, 102, 102),
                              self.playingfield.decoration[i], self.playingfield.dotsize, "plus")

        for i in range(self.settings.playeramount):
            player = Player(self.settings.piececolors[i],
                            self.settings.housecolors[i],
                            self.settings.starttilecolors[i],
                            self.settings.pieceamount, self.playingfield.dotsize)

            self.players.append(player)

        for i in range(len(self.playingfield.fieldTiles)):
            Renderer().render(self.playingfield.color,
                              self.playingfield.fieldTiles[i].tileCoords,
                              self.playingfield.dotsize, "star")

        for x in range(self.settings.playeramount):
            Renderer().render(self.players[x].startTileColor,
                              self.playingfield.fieldTiles[self.playingfield.starttileids[x]].tileCoords,
                              self.playingfield.dotsize, "star")
            for i in range(self.settings.pieceamount):
                Renderer().render(self.players[x].houseColor,
                                  self.playingfield.endhouses[x][i].tileCoords,
                                  self.playingfield.dotsize, "questionmark")

                Renderer().render(self.players[x].houseColor,
                                  self.playingfield.starthouses[x][i].tileCoords,
                                  self.playingfield.dotsize, "questionmark")

        for i in range(self.settings.playeramount):
            for x in range(self.settings.pieceamount):
                self.players[i].playerPieces[x].placepiece(
                    self.playingfield.starthouses[i][x].tileCoords)

        Renderer().inithighlight(self.playingfield.dotsize)

        Renderer().refreshui(self.playingfield.canvassize[1], self.settings.playernames[self.playerchoice], self.piecechoice, self.roll, int(windowsize / fontsizefactor), Settings.playernames,
                             self.statetext)
        position = self.players[self.playerchoice].playerPieces[self.piecechoice].position
        Renderer().highlight((position[0] + 0.5, position[1] + 0.5))

        t.tracer(True)

    # Debug method for randomly placing pieces on the field
    def shufflepieces(self):
        for i in range(self.settings.playeramount):
            for x in range(self.settings.pieceamount):
                if x != 0:
                    piecetoshuffle = self.players[i].playerPieces[x]
                    placement = random.randrange(
                        0, len(self.playingfield.fieldTiles))

                    if self.playingfield.fieldTiles[placement].tilestandingplayer is None:
                        piecetoshuffle.movepiece(
                            self.playingfield.fieldTiles[placement].tileCoords)
                        self.playingfield.fieldTiles[placement].tilestandingplayer = i
                        self.playingfield.fieldTiles[placement].tilestandingpiece = x

    # Method for kicking pieces from the playing field back into starter houses
    def kickpiece(self, teamtokick, piecetokick):
        self.players[teamtokick].playerPieces[piecetokick].movepiece(
            self.playingfield.starthouses[teamtokick][piecetokick].tileCoords)
        self.players[teamtokick].playerPieces[piecetokick].positioninplayingfield = None
        self.players[teamtokick].playerPieces[piecetokick].tilesmoved = 0

    # Method for placing piece on the field from the start house
    def initiatepiece(self):
        self.currentGameState = GAMESTATE_AWAIT
        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        startingtile = self.playingfield.fieldTiles[self.playingfield.starttileids[self.playerchoice]]

        if startingtile.tilestandingplayer is self.playerchoice:
            return False

        piece.positioninplayingfield = self.playingfield.starttileids[self.playerchoice]
        piece.tilesmoved = 1
        piece.movepiece(
            self.playingfield.fieldTiles[self.playingfield.starttileids[self.playerchoice]].tileCoords)
        if startingtile.tilestandingplayer is not None:
            self.kickpiece(startingtile.tilestandingplayer,
                           startingtile.tilestandingpiece)
        self.playingfield.fieldTiles[
            self.playingfield.starttileids[self.playerchoice]].tilestandingplayer = self.playerchoice
        self.playingfield.fieldTiles[
            self.playingfield.starttileids[self.playerchoice]].tilestandingpiece = self.piecechoice

        return True

    # Method for moving pieces on the playing field
    def iteratetroughfield(self, looprange):
        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        for i in range(looprange):
            piece.tilesmoved += 1
            piece.positioninplayingfield += 1
            piece.movepiece(
                self.playingfield.fieldTiles[piece.positioninplayingfield].tileCoords)

    # Method for moving pieces inside end houses
    def iteratetroughhouse(self, looprange):
        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        for i in range(looprange):
            piece.positioninhouse += 1
            piece.movepiece(
                self.playingfield.endhouses[self.playerchoice][piece.positioninhouse].tileCoords)

    def notifytileofpeice(self):
        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        self.playingfield.fieldTiles[piece.positioninplayingfield].tilestandingplayer = self.playerchoice
        self.playingfield.fieldTiles[piece.positioninplayingfield].tilestandingpiece = self.piecechoice

    def removepiecefromtile(self):
        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        self.playingfield.fieldTiles[piece.positioninplayingfield].tilestandingplayer = None
        self.playingfield.fieldTiles[piece.positioninplayingfield].tilestandingpiece = None

    def notifyhouseofpiece(self):
        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        self.playingfield.endhouses[self.playerchoice][piece.positioninhouse].tilestandingpiece = self.piecechoice

    def removepiecefromhouse(self):
        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        self.playingfield.endhouses[self.playerchoice][piece.positioninhouse].tilestandingpiece = None

    # Method with logic and rules for moving pieces.
    def performmovement(self, roll):
        self.currentGameState = GAMESTATE_AWAIT

        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        # If the move results in a piece going outside the playing field or end house, the move gets skipped
        if piece.tilesmoved + roll + piece.positioninhouse > self.lenghtoftravel - 1 + self.settings.pieceamount:
            return MOVESTATE_OUTOFBOUNDS

        # If the move results in the piece exceeding the lenght of travel needed to get into a house
        if piece.tilesmoved + roll > self.lenghtoftravel:
            currenttilesmoved = piece.tilesmoved
            housedifference = self.lenghtoftravel - piece.tilesmoved
            if piece.isinhouse is True:
                currentposition = self.playingfield.endhouses[self.playerchoice][piece.positioninhouse]
            else:
                currentposition = self.playingfield.fieldTiles[piece.positioninplayingfield]
        
            futureposition = self.playingfield.endhouses[self.playerchoice][piece.positioninhouse + (roll - housedifference)]
        
            # if the tile inside the house is already occupied, the move gets skipped
            if futureposition.tilestandingpiece is not None:
                self.iteratetroughfield(housedifference)
                self.iteratetroughhouse(roll - housedifference)
                piece.tilesmoved = currenttilesmoved
                if piece.isinhouse is False:
                    piece.positioninplayingfield = currentposition.tileID
                    piece.positioninhouse = -1
                    piece.movepiece(currentposition.tileCoords)
                else:
                    piece.positioninhouse = currentposition.tileID
                    piece.movepiece(currentposition.tileCoords)
        
                return MOVESTATE_TILEOCCUPIED
        
            self.removepiecefromhouse()
            self.iteratetroughfield(housedifference)
            self.iteratetroughhouse(roll - housedifference)
            self.notifyhouseofpiece()
            if piece.isinhouse is False:
                self.playingfield.fieldTiles[piece.positioninplayingfield].tilestandingplayer = None
            piece.isinhouse = True
            return MOVESTATE_SUCCESS

        self.removepiecefromtile()
        difference = (piece.positioninplayingfield + roll) - \
            (self.lenghtoftravel - 1)
        difference = max(0, difference)
        currenttilesmoved = piece.tilesmoved
        currentposition = self.playingfield.fieldTiles[piece.positioninplayingfield]
        
        if difference > 0:
            futureposition = self.playingfield.fieldTiles[difference - 1]
        
        else:
            futureposition = self.playingfield.fieldTiles[piece.positioninplayingfield + roll]

        # if the tile inside the playing field is occupied by a piece of the same player, the move gets skipped

        self.iteratetroughfield(roll - difference)
        if difference > 0:
            piece.positioninplayingfield = -1
            self.iteratetroughfield(difference)

        if futureposition.tilestandingplayer == self.playerchoice:
            piece.tilesmoved = currenttilesmoved
            piece.positioninplayingfield = currentposition.tileID
            piece.movepiece(currentposition.tileCoords)
            self.notifytileofpeice()
            return MOVESTATE_TILEOCCUPIED
        
        # if the tile inside the playing field is occupied by a piece of another player, the peice gets kicked out
        elif futureposition.tilestandingplayer != self.playerchoice:
            if futureposition.tilestandingplayer is None:
                self.notifytileofpeice()
                return MOVESTATE_SUCCESS

            if futureposition.tileID == self.playingfield.starttileids[futureposition.tilestandingplayer]:
                piece.movepiece(currentposition.tileCoords)
                piece.positioninplayingfield = currentposition.tileID
                self.notifytileofpeice()
                return MOVESTATE_TILEOCCUPIED

            self.kickpiece(futureposition.tilestandingplayer, futureposition.tilestandingpiece)
            self.notifytileofpeice()
            return MOVESTATE_SUCCESS

        self.notifytileofpeice()
        return MOVESTATE_SUCCESS

    def refreshui(self):
        Renderer().refreshui(self.playingfield.canvassize[1], self.settings.playernames[self.playerchoice], self.piecechoice, self.roll, gamefont[1], self.settings.playernames, self.statetext)
