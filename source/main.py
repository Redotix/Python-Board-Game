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

lenghtoftravel = len(playingfield.fieldTiles)
playerchoice = 0
piecechoice = 0
rollnum = 0
attempt = 0


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


# Method for kicking pieces from the playing field back into starter houses
def kickpiece(teamtokick, piecetokick):
    players[teamtokick].playerPieces[piecetokick].movepiece(
        playingfield.starthouses[teamtokick][piecetokick].tileCoords)
    players[teamtokick].playerPieces[piecetokick].positioninplayingfield = None
    players[teamtokick].playerPieces[piecetokick].tilesmoved = 0


# Method for placing piece on the field from the start house
def initiatepiece():
    piece = players[playerchoice].playerPieces[piecechoice]

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
    piece = players[playerchoice].playerPieces[piecechoice]

    for i in range(looprange):
        piece.tilesmoved += 1
        piece.positioninplayingfield += 1
        piece.movepiece(playingfield.fieldTiles[piece.positioninplayingfield].tileCoords)


# Method for moving pieces inside end houses
def iteratetroughhouse(looprange):
    piece = players[playerchoice].playerPieces[piecechoice]

    for i in range(looprange):
        piece.positioninhouse += 1
        piece.movepiece(playingfield.endhouses[playerchoice][piece.positioninhouse].tileCoords)


def notifytileofpeice():
    piece = players[playerchoice].playerPieces[piecechoice]

    playingfield.fieldTiles[piece.positioninplayingfield].tilestandingplayer = playerchoice
    playingfield.fieldTiles[piece.positioninplayingfield].tilestandingpiece = piecechoice


def removepiecefromtile():
    piece = players[playerchoice].playerPieces[piecechoice]

    playingfield.fieldTiles[piece.positioninplayingfield].tilestandingplayer = None
    playingfield.fieldTiles[piece.positioninplayingfield].tilestandingpiece = None


def notifyhouseofpiece():
    piece = players[playerchoice].playerPieces[piecechoice]

    playingfield.endhouses[playerchoice][piece.positioninhouse].tilestandingpiece = piecechoice


def removepiecefromhouse():
    piece = players[playerchoice].playerPieces[piecechoice]

    playingfield.endhouses[playerchoice][piece.positioninhouse].tilestandingpiece = None


# Method with logic and rules for moving pieces.
def performmovement(roll):
    piece = players[playerchoice].playerPieces[piecechoice]

    # If the move results in a piece going outside the playing field or end house, the move gets skipped
    if piece.tilesmoved + roll + piece.positioninhouse > lenghtoftravel - 1 + settings.pieceamount:
        return False

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
            return True

        removepiecefromhouse()
        iteratetroughfield(housedifference)
        iteratetroughhouse(roll - housedifference)
        notifyhouseofpiece()
        if piece.isinhouse is False:
            playingfield.fieldTiles[piece.positioninplayingfield].tilestandingplayer = None
        piece.isinhouse = True
        return False

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
        return False

    # if the tile inside the playing field is occupied by a piece of another player, the peice gets kicked out
    elif futureposition.tilestandingplayer != playerchoice and futureposition.tilestandingplayer is not None:
        iteratetroughfield(roll - difference)
        if difference > 0:
            piece.positioninplayingfield = -1
            iteratetroughfield(difference)
        kickpiece(futureposition.tilestandingplayer, futureposition.tilestandingpiece)
        notifytileofpeice()
        return True

    iteratetroughfield(roll - difference)
    if difference > 0:
        piece.positioninplayingfield = -1
        iteratetroughfield(difference)

    notifytileofpeice()
    return True


def printstate():
    global playerchoice
    global piecechoice

    print("Its player ", playerchoice, "'s turn.")
    print("Piece number ", piecechoice, " is chosen")


def cyclepiecesright(pieceamount):
    global piecechoice

    if piecechoice + 1 > pieceamount - 1:
        piecechoice = 0
    else:
        piecechoice += 1

    printstate()


def cyclepiecesleft(pieceamount):
    global piecechoice

    if piecechoice - 1 < 0:
        piecechoice = pieceamount - 1
    else:
        piecechoice -= 1

    printstate()


def cycleplayers(playeramount):
    global playerchoice

    if playerchoice + 1 > playeramount - 1:
        playerchoice = 0
    else:
        playerchoice += 1

    printstate()


def skipturn(playeramount):
    cycleplayers(playeramount)
    print("You skipped your turn")


def moveattempt(playeramount):
    global rollnum
    global attempt
    piecesonboard = None

    piece = players[playerchoice].playerPieces[piecechoice]

    if rollnum == 0:
        rollnum = random.randrange(1, 7)

    for i in range(10):
        print()
    print("Rolled: ", rollnum)

    for i in range(len(players[playerchoice].playerPieces)):
        if players[playerchoice].playerPieces[i].positioninplayingfield is not None:
            piecesonboard = True
        elif piecesonboard is not True:
            piecesonboard = False

    print("piece on board is ", piecesonboard)

    if piecesonboard is False and rollnum == 6:
        initiatepiece()
        cycleplayers(playeramount)
        rollnum = 0
        attempt = 0
        print("Placed piece of playing field")
        return

    elif piecesonboard is False and rollnum != 6:
        if attempt + 1 > 2:
            rollnum = 0
            attempt = 0
            cycleplayers(playeramount)
            print("Out of attempts, turn skipped")
        else:
            rollnum = 0
            attempt += 1
            print("Didnt throw 6, you have another attempt")
        return

    if piece.positioninplayingfield is None and rollnum == 6:
        initiatepiece()
        cycleplayers(playeramount)
        rollnum = 0
        print("Placed piece of playing field")
        return

    elif piece.positioninplayingfield is None and rollnum != 6:
        print("Didnt roll a 6, choose a different piece or skip turn")
        return

    answer = performmovement(rollnum)
    if answer is True:
        cycleplayers(playeramount)
        rollnum = 0
        print("Moved piece")
        return
    print("Piece cant move there, choose a different piece or skip turn")


win.onkey(lambda: cyclepiecesleft(settings.pieceamount), "Left")
win.onkey(lambda: cyclepiecesright(settings.pieceamount), "Right")
win.onkey(lambda: moveattempt(settings.playeramount), "Return")
win.onkey(lambda: skipturn(settings.playeramount), "s")
win.listen()

win.mainloop()
