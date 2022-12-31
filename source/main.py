from Settings import *
from Renderer import *
from PlayField import *
from Player import *
import random


def inputsettings():
    playeramount = 4
    pieceamount = 4
    extratiles = 3
    return Settings(playeramount, pieceamount, extratiles)


settings = inputsettings()
playingfield = PlayField()

playingfield.generatefield(settings.extratiles)

win = t.Screen()
win.setup(600, 600)
win.setworldcoordinates(0, 0, playingfield.canvassize[1], playingfield.canvassize[0])
win.bgcolor("grey")
t.colormode(255)

players = []


def initializescreen():
    t.tracer(False)

    for i in range(settings.playeramount):
        player = Player(settings.piececolors[i],
                        settings.housecolors[i],
                        settings.starttilecolors[i],
                        settings.pieceamount, playingfield.dotsize, playingfield.starttileids[i])

        players.append(player)

    for i in range(len(playingfield.fieldTiles)):
        Renderer().render(playingfield.color,
                          playingfield.fieldTiles[i].tileCoords,
                          playingfield.dotsize, "star")

    for x in range(settings.playeramount):
        Renderer().render(players[x].startTileColor,
                          playingfield.fieldTiles[playingfield.starttileids[x]].tileCoords,
                          playingfield.dotsize, "star")
        for i in range(settings.pieceamount):
            Renderer().render(players[x].houseColor,
                              playingfield.endhouses[x][i].tileCoords,
                              playingfield.dotsize, "questionmark")

            Renderer().render(players[x].houseColor,
                              playingfield.starthouses[x][i].tileCoords,
                              playingfield.dotsize, "questionmark")

    for i in range(settings.playeramount):
        for x in range(settings.pieceamount):
            players[i].playerPieces[x].placepiece(playingfield.starthouses[i][x].tileCoords)

    t.tracer(True)


initializescreen()

lenghtoftravel = len(playingfield.fieldTiles)
playerchoice = 1
piecechoice = 2


def iteratetroughfield(looprange):
    for i in range(looprange):
        players[playerchoice].playerPieces[piecechoice].movepiece(
            playingfield.fieldTiles[players[playerchoice].playerPieces[piecechoice].positioninplayingfield].tileCoords)
        players[playerchoice].playerPieces[piecechoice].tilesmoved += 1
        players[playerchoice].playerPieces[piecechoice].positioninplayingfield += 1


def iteratetroughhouse(looprange):
    for i in range(looprange):
        players[playerchoice].playerPieces[piecechoice].movepiece(
            playingfield.endhouses[playerchoice]
            [players[playerchoice].playerPieces[piecechoice].positioninhouse].tileCoords)
        players[playerchoice].playerPieces[piecechoice].tilesmoved += 1
        players[playerchoice].playerPieces[piecechoice].positioninhouse += 1


def debugmove():
    roll = random.randrange(1, 7)
    difference = (players[playerchoice].playerPieces[piecechoice].positioninplayingfield + roll) - lenghtoftravel
    difference = max(0, difference)
    if players[playerchoice].playerPieces[piecechoice].tilesmoved + roll > lenghtoftravel and \
            players[playerchoice].playerPieces[piecechoice].isinhouse is False:
        housedifference = lenghtoftravel - players[playerchoice].playerPieces[piecechoice].tilesmoved
        iteratetroughfield(housedifference)
        iteratetroughhouse(roll - housedifference)
        players[playerchoice].playerPieces[piecechoice].isinhouse = True
    elif players[playerchoice].playerPieces[piecechoice].isinhouse is False:
        iteratetroughfield(roll - difference)

        if difference > 0:
            players[playerchoice].playerPieces[piecechoice].positioninplayingfield = 0
            iteratetroughfield(difference)

    for i in range(10):
        print()
    print("Rolled: ", roll)
    print("Difference was: ", difference)
    print("Total tiles moved: ", players[playerchoice].playerPieces[piecechoice].tilesmoved)
    print("Real position on playing field: ", players[playerchoice].playerPieces[piecechoice].positioninplayingfield)


# def turn():
#     global playerchoice
#     global piecechoice
#     playerchoice += 1
#     piecechoice = 0
#     if playerchoice == len(players):
#         playerchoice = 0
#
#
# def nextpiece():
#     global piecechoice
#     piecechoice += 1
#     if piecechoice == len(players[0].playerPieces):
#         piecechoice = 0
#
#
# def previouspiece():
#     global piecechoice
#     piecechoice -= 1
#     if piecechoice == -1:
#         piecechoice = len(players[0].playerPieces) - 1


# def renderinfo():
#     t.tracer(False)
#     player = "Player " + str(playerchoice + 1) + "'s turn."
#     piece = "Piece " + str(piecechoice + 1)
#     Renderer().writingTurtle.clear()
#     Renderer().drawtext(player, (0, 0), 12)
#     Renderer().drawtext(piece, (0, 1), 12)
#     t.tracer(True)


# turn()
# win.onkey(nextpiece, "Right")
# win.onkey(previouspiece, "Left")
win.onkey(debugmove, "Return")
win.listen()

win.mainloop()
