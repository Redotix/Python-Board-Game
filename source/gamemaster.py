from Settings import *
from Renderer import *
from PlayField import *
from Player import *
import random

win = t.Screen()
win.setup(600, 600)
t.colormode(255)
win.bgcolor((128, 128, 128))


class GameMaster:
    settings = None
    playingfield = PlayField()

    players = []
    lenghtoftravel = len(playingfield.fieldTiles)
    playerchoice = 0
    piecechoice = 0
    inmenu = True

    data = None

    def __init__(self, playeramount, pieceamount, extratiles):
        t.tracer(False)
        self.settings = Settings(playeramount, pieceamount, extratiles)

        self.playingfield.generatefield(self.settings.extratiles)
        win.setworldcoordinates(0, 0, self.playingfield.canvassize[1], self.playingfield.canvassize[0])

        for i in range(len(self.playingfield.decoration)):
            Renderer().render((102, 102, 102), self.playingfield.decoration[i], self.playingfield.dotsize, "plus")

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
                self.players[i].playerPieces[x].placepiece(self.playingfield.starthouses[i][x].tileCoords)

        Renderer().inithighlight(self.playingfield.dotsize)
        Renderer().refreshui(self.playingfield.canvassize[0],
                             self.settings.playernames[self.playerchoice],
                             self.piecechoice, 0)

        t.tracer(True)

    # Debug method for randomly placing pieces on the field
    def shufflepieces(self):
        for i in range(self.settings.playeramount):
            for x in range(self.settings.pieceamount):
                if x != 0:
                    piecetoshuffle = self.players[i].playerPieces[x]
                    placement = random.randrange(0, len(self.playingfield.fieldTiles))

                    if self.playingfield.fieldTiles[placement].tilestandingplayer is None:
                        piecetoshuffle.movepiece(self.playingfield.fieldTiles[placement].tileCoords)
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

        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        startingtile = self.playingfield.fieldTiles[self.playingfield.starttileids[self.playerchoice]]
        piece.positioninplayingfield = self.playingfield.starttileids[self.playerchoice]
        piece.tilesmoved = 1
        piece.movepiece(self.playingfield.fieldTiles[self.playingfield.starttileids[self.playerchoice]].tileCoords)
        if startingtile.tilestandingplayer is not None:
            self.kickpiece(startingtile.tilestandingplayer, startingtile.tilestandingpiece)
        self.playingfield.fieldTiles[
            self.playingfield.starttileids[self.playerchoice]].tilestandingplayer = self.playerchoice
        self.playingfield.fieldTiles[
            self.playingfield.starttileids[self.playerchoice]].tilestandingpiece = self.piecechoice

    # Method for moving pieces on the playing field
    def iteratetroughfield(self, looprange):
        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        for i in range(looprange):
            piece.tilesmoved += 1
            piece.positioninplayingfield += 1
            piece.movepiece(self.playingfield.fieldTiles[piece.positioninplayingfield].tileCoords)

    # Method for moving pieces inside end houses
    def iteratetroughhouse(self, looprange):
        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        for i in range(looprange):
            piece.positioninhouse += 1
            piece.movepiece(self.playingfield.endhouses[self.playerchoice][piece.positioninhouse].tileCoords)

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

        piece = self.players[self.playerchoice].playerPieces[self.piecechoice]

        # If the move results in a piece going outside the playing field or end house, the move gets skipped
        if piece.tilesmoved + roll + piece.positioninhouse > self.lenghtoftravel - 1 + self.settings.pieceamount:
            return False

        # If the move results in the piece exceeding the lenght of travel needed to get into a house
        if piece.tilesmoved + roll > self.lenghtoftravel:
            currenttilesmoved = piece.tilesmoved
            housedifference = self.lenghtoftravel - piece.tilesmoved
            if piece.isinhouse is True:
                currentposition = self.playingfield.endhouses[self.playerchoice][piece.positioninhouse]
            else:
                currentposition = self.playingfield.fieldTiles[piece.positioninplayingfield]

            futureposition = self.playingfield.endhouses[
                self.playerchoice][piece.positioninhouse + (roll - housedifference)]

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

                return True

            self.removepiecefromhouse()
            self.iteratetroughfield(housedifference)
            self.iteratetroughhouse(roll - housedifference)
            self.notifyhouseofpiece()
            if piece.isinhouse is False:
                self.playingfield.fieldTiles[piece.positioninplayingfield].tilestandingplayer = None
            piece.isinhouse = True
            return False

        self.removepiecefromtile()
        difference = (piece.positioninplayingfield + roll) - (self.lenghtoftravel - 1)
        difference = max(0, difference)
        currenttilesmoved = piece.tilesmoved
        currentposition = self.playingfield.fieldTiles[piece.positioninplayingfield]

        if difference > 0:
            futureposition = self.playingfield.fieldTiles[difference - 1]

        else:
            futureposition = self.playingfield.fieldTiles[piece.positioninplayingfield + roll]

        # if the tile inside the playing field is occupied by a piece of the same player, the move gets skipped
        if futureposition.tilestandingplayer == self.playerchoice:
            self.iteratetroughfield(roll - difference)
            if difference > 0:
                piece.positioninplayingfield = -1
                self.iteratetroughfield(difference)
            piece.tilesmoved = currenttilesmoved
            piece.positioninplayingfield = currentposition.tileID
            piece.movepiece(currentposition.tileCoords)
            self.notifytileofpeice()
            return False

        # if the tile inside the playing field is occupied by a piece of another player, the peice gets kicked out
        elif futureposition.tilestandingplayer != self.playerchoice and futureposition.tilestandingplayer is not None:
            self.iteratetroughfield(roll - difference)
            if difference > 0:
                piece.positioninplayingfield = -1
                self.iteratetroughfield(difference)
            self.kickpiece(futureposition.tilestandingplayer, futureposition.tilestandingpiece)
            self.notifytileofpeice()
            return True

        self.iteratetroughfield(roll - difference)
        if difference > 0:
            piece.positioninplayingfield = -1
            self.iteratetroughfield(difference)

        self.notifytileofpeice()
        return True


# def printstate():
#     global playerchoice
#     global piecechoice
#
#     print("Its player ", playerchoice, "'s turn.")
#     print("Piece number ", piecechoice, " is chosen")
#
#
# def cyclepiecesright(pieceamount):
#     global piecechoice
#
#     if piecechoice + 1 > pieceamount - 1:
#         piecechoice = 0
#     else:
#         piecechoice += 1
#
#     printstate()
#
#
# def cyclepiecesleft(pieceamount):
#     global piecechoice
#
#     if piecechoice - 1 < 0:
#         piecechoice = pieceamount - 1
#     else:
#         piecechoice -= 1
#
#     printstate()
#
#
# def cycleplayers(playeramount):
#     global playerchoice
#
#     if playerchoice + 1 > playeramount - 1:
#         playerchoice = 0
#     else:
#         playerchoice += 1
#
#     printstate()
#
#
# def skipturn(playeramount):
#     cycleplayers(playeramount)
#     print("You skipped your turn")
#
#
# def moveattempt(playeramount):
#     global rollnum
#     global attempt
#     piecesonboard = None
#
#     piece = players[playerchoice].playerPieces[piecechoice]
#
#     if rollnum == 0:
#         rollnum = random.randrange(1, 7)
#
#     for i in range(10):
#         print()
#     print("Rolled: ", rollnum)
#
#     for i in range(len(players[playerchoice].playerPieces)):
#         if players[playerchoice].playerPieces[i].positioninplayingfield is not None:
#             piecesonboard = True
#         elif piecesonboard is not True:
#             piecesonboard = False
#
#     print("piece on board is ", piecesonboard)
#
#     if piecesonboard is False and rollnum == 6:
#         initiatepiece()
#         cycleplayers(playeramount)
#         rollnum = 0
#         attempt = 0
#         print("Placed piece of playing field")
#         return
#
#     elif piecesonboard is False and rollnum != 6:
#         if attempt + 1 > 2:
#             rollnum = 0
#             attempt = 0
#             cycleplayers(playeramount)
#             print("Out of attempts, turn skipped")
#         else:
#             rollnum = 0
#             attempt += 1
#             print("Didnt throw 6, you have another attempt")
#         return
#
#     if piece.positioninplayingfield is None and rollnum == 6:
#         initiatepiece()
#         cycleplayers(playeramount)
#         rollnum = 0
#         print("Placed piece of playing field")
#         return
#
#     elif piece.positioninplayingfield is None and rollnum != 6:
#         print("Didnt roll a 6, choose a different piece or skip turn")
#         return
#
#     answer = performmovement(rollnum)
#     if answer is True:
#         cycleplayers(playeramount)
#         rollnum = 0
#         print("Moved piece")
#         return
#     print("Piece cant move there, choose a different piece or skip turn")
#
#
# win.onkey(lambda: cyclepiecesleft(settings.pieceamount), "Left")
# win.onkey(lambda: cyclepiecesright(settings.pieceamount), "Right")
# win.onkey(lambda: moveattempt(settings.playeramount), "Return")
# win.onkey(lambda: skipturn(settings.playeramount), "s")
