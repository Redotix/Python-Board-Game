from Settings import *
from Renderer import *
from PlayField import *
from Player import *
import random


win = t.Screen()
win.setup(600, 600)
win.bgcolor("grey")
t.colormode(255)


def inputsettings():
    playeramount = 4
    pieceamount = 4
    extratiles = 3
    return Settings(playeramount, pieceamount, extratiles)


settings = inputsettings()
playingfield = PlayField()

playingfield.generatefield(settings.extratiles)

win.setworldcoordinates(0, 0, playingfield.canvassize[1], playingfield.canvassize[0])

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
playerchoice = 0
piecechoice = 0

piece = players[playerchoice].playerPieces[piecechoice]


# Debug method for randomly placing pieces on the field
def shufflepieces():
    for i in range(settings.playeramount):
        for x in range(settings.pieceamount):
            if x != 0:
                piecetoshuffle = players[i].playerPieces[x]
                placement = random.randrange(0, len(playingfield.fieldTiles))

                if playingfield.fieldTiles[placement].tilestandingplayer is None:
                    piecetoshuffle.movepiece(playingfield.fieldTiles[placement].tileCoords)
                    playingfield.fieldTiles[placement].tilestandingplayer = i
                    playingfield.fieldTiles[placement].tilestandingpiece = x


# players[0].playerPieces[1].placepiece(playingfield.endhouses[0][0].tileCoords)
# playingfield.endhouses[0][0].tilestandingpiece = 1
# players[0].playerPieces[2].placepiece(playingfield.endhouses[0][1].tileCoords)
# playingfield.endhouses[0][1].tilestandingpiece = 2
# players[0].playerPieces[3].placepiece(playingfield.endhouses[0][3].tileCoords)
# playingfield.endhouses[0][3].tilestandingpiece = 3

# Method for kicking pieces from the playing field back into starter houses
def kickpiece(teamtokick, piecetokick):
    players[teamtokick].playerPieces[piecetokick].movepiece(
        playingfield.starthouses[teamtokick][piecetokick].tileCoords)
    players[teamtokick].playerPieces[piecetokick].positioninplayingfield = None
    players[teamtokick].playerPieces[piecetokick].tilesmoved = 0


# Method for placing piece on the field from the start house
def initiatepiece():
    startingtile = playingfield.fieldTiles[playingfield.starttileids[playerchoice]]
    piece.positioninplayingfield = playingfield.starttileids[playerchoice]
    piece.tilesmoved = 1
    piece.movepiece(playingfield.fieldTiles[playingfield.starttileids[playerchoice]].tileCoords)
    if startingtile.tilestandingplayer is not None:
        kickpiece(startingtile.tilestandingplayer, startingtile.tilestandingpiece)
    playingfield.fieldTiles[playingfield.starttileids[playerchoice]].tilestandingplayer = playerchoice
    playingfield.fieldTiles[playingfield.starttileids[playerchoice]].tilestandingpiece = piecechoice


# Method for moving pieces on the playing field
def iteratetroughfield(looprange):
    for i in range(looprange):
        piece.tilesmoved += 1
        piece.positioninplayingfield += 1
        piece.movepiece(playingfield.fieldTiles[piece.positioninplayingfield].tileCoords)


# Method for moving pieces inside end houses
def iteratetroughhouse(looprange):
    for i in range(looprange):
        piece.positioninhouse += 1
        piece.movepiece(playingfield.endhouses[playerchoice][piece.positioninhouse].tileCoords)


def notifytileofpeice():
    playingfield.fieldTiles[piece.positioninplayingfield].tilestandingplayer = playerchoice
    playingfield.fieldTiles[piece.positioninplayingfield].tilestandingpiece = piecechoice


def removepiecefromtile():
    playingfield.fieldTiles[piece.positioninplayingfield].tilestandingplayer = None
    playingfield.fieldTiles[piece.positioninplayingfield].tilestandingpiece = None


def notifyhouseofpiece():
    playingfield.endhouses[playerchoice][piece.positioninhouse].tilestandingpiece = piecechoice


def removepiecefromhouse():
    playingfield.endhouses[playerchoice][piece.positioninhouse].tilestandingpiece = None


# Method with logic and rules for moving pieces.
def performmovement(roll):
    for i in range(10):
        print()
    print("Rolled: ", roll)

    # If the move results in a piece going outside the playing field or end house, the move gets skipped
    if piece.tilesmoved + roll + piece.positioninhouse > lenghtoftravel - 1 + settings.pieceamount:
        return

    # If the move results in the piece exceeding the lenght of travel needed to get into a house
    if piece.tilesmoved + roll > lenghtoftravel:
        currenttilesmoved = piece.tilesmoved
        housedifference = lenghtoftravel - piece.tilesmoved
        if piece.isinhouse is True:
            currentposition = playingfield.endhouses[playerchoice][piece.positioninhouse]
        else:
            currentposition = playingfield.fieldTiles[piece.positioninplayingfield]

        futureposition = playingfield.endhouses[playerchoice][piece.positioninhouse + (roll - housedifference)]

        # if the tile inside the house is already occupied, the move gets skipped
        if futureposition.tilestandingpiece is not None:
            iteratetroughfield(housedifference)
            iteratetroughhouse(roll - housedifference)
            piece.tilesmoved = currenttilesmoved
            if piece.isinhouse is False:
                piece.positioninplayingfield = currentposition.tileID
                piece.positioninhouse = -1
                piece.movepiece(currentposition.tileCoords)
            else:
                piece.positioninhouse = currentposition.tileID
                piece.movepiece(currentposition.tileCoords)
            return

        removepiecefromhouse()
        iteratetroughfield(housedifference)
        iteratetroughhouse(roll - housedifference)
        notifyhouseofpiece()
        if piece.isinhouse is False:
            playingfield.fieldTiles[piece.positioninplayingfield].tilestandingplayer = None
        piece.isinhouse = True
        return

    removepiecefromtile()
    difference = (piece.positioninplayingfield + roll) - (lenghtoftravel - 1)
    difference = max(0, difference)
    currenttilesmoved = piece.tilesmoved
    currentposition = playingfield.fieldTiles[piece.positioninplayingfield]

    if difference > 0:
        futureposition = playingfield.fieldTiles[difference - 1]

    else:
        futureposition = playingfield.fieldTiles[piece.positioninplayingfield + roll]

    # if the tile inside the playing field is occupied by a piece of the same player, the move gets skipped
    if futureposition.tilestandingplayer == playerchoice:
        iteratetroughfield(roll - difference)
        if difference > 0:
            piece.positioninplayingfield = -1
            iteratetroughfield(difference)
        piece.tilesmoved = currenttilesmoved
        piece.positioninplayingfield = currentposition.tileID
        piece.movepiece(currentposition.tileCoords)
        notifytileofpeice()
        return

    # if the tile inside the playing field is occupied by a piece of another player, the peice gets kicked out
    elif futureposition.tilestandingplayer != playerchoice and futureposition.tilestandingplayer is not None:
        iteratetroughfield(roll - difference)
        if difference > 0:
            piece.positioninplayingfield = -1
            iteratetroughfield(difference)
        kickpiece(futureposition.tilestandingplayer, futureposition.tilestandingpiece)
        notifytileofpeice()
        return

    iteratetroughfield(roll - difference)
    if difference > 0:
        piece.positioninplayingfield = -1
        iteratetroughfield(difference)

    notifytileofpeice()

    print("Difference was: ", difference)
    print("Total tiles moved: ", piece.tilesmoved)
    print("Real position on playing field: ", piece.positioninplayingfield)


def debugkey():
    roll = random.randrange(1, 7)
    performmovement(roll)
    print(players[2].playerPieces[0].isinhouse)


# shufflepieces()
initiatepiece()

for q in range(len(playingfield.fieldTiles)):
    if playingfield.fieldTiles[q].tilestandingplayer is not None:
        print("field tile", q, playingfield.fieldTiles[q].tileCoords, playingfield.fieldTiles[q].tilestandingpiece)
# turn()
# win.onkey(nextpiece, "Right")
# win.onkey(previouspiece, "Left")
win.onkey(debugkey, "Return")
win.listen()

win.mainloop()
