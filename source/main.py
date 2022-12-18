from Settings import *
from Renderer import *
from PlayField import *
from Player import *


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
                        settings.pieceamount, playingfield.dotsize)

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

lenghtoftravel = len(playingfield.fieldTiles) - 1


def debugmove():
    playerinput = 0
    pieceinput = 0
    print(players[playerinput].playerPieces[pieceinput].currentpos)
    if players[playerinput].playerPieces[pieceinput].currentpos is None:
        players[playerinput].playerPieces[pieceinput].movepiece(
            playingfield.fieldTiles[playingfield.starttileids[playerinput]].tileCoords)
        players[playerinput].playerPieces[pieceinput].currentpos = 1

    elif players[playerinput].playerPieces[pieceinput].currentpos == lenghtoftravel:
        players[playerinput].playerPieces[pieceinput].currentpos -= lenghtoftravel
        players[playerinput].playerPieces[pieceinput].movepiece(
            playingfield.endhouses[playerinput][players[playerinput].playerPieces[pieceinput].currentpos].tileCoords)
        players[playerinput].playerPieces[pieceinput].currentpos += 1
        players[playerinput].playerPieces[pieceinput].isfinished = True

    elif players[playerinput].playerPieces[pieceinput].isfinished is not True:
        if players[playerinput].playerPieces[pieceinput].currentpos + \
                playingfield.starttileids[playerinput] + 1 \
                < len(playingfield.fieldTiles):

            players[playerinput].playerPieces[pieceinput].movepiece(
                playingfield.fieldTiles[playingfield.starttileids[playerinput] +
                                        players[playerinput].playerPieces[pieceinput].currentpos].tileCoords)
            players[playerinput].playerPieces[pieceinput].currentpos += 1

        else:
            players[playerinput].playerPieces[pieceinput].currentpos -= len(playingfield.fieldTiles)
            players[playerinput].playerPieces[pieceinput].movepiece(
                playingfield.fieldTiles[playingfield.starttileids[playerinput] +
                                        players[playerinput].playerPieces[pieceinput].currentpos].tileCoords)
            players[playerinput].playerPieces[pieceinput].currentpos += 1


for loop in range(43):
    debugmove()

win.mainloop()
