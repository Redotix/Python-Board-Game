from gamemaster import *


def highlightpiece(x, y):
    position = (int(x), int(y))

    piecelist = master.players[master.playerchoice].playerPieces
    for pi in range(len(piecelist)):
        if position == piecelist[pi].position:
            Renderer().highlight((position[0] + 0.5, position[1] + 0.5))
            return

        Renderer().hidehighlight()


def cyclepiecesright():
    if master.piecechoice + 1 > master.settings.pieceamount - 1:
        master.piecechoice = 0
    else:
        master.piecechoice += 1

    pos = master.players[master.playerchoice].playerPieces[master.piecechoice].position
    Renderer().highlight((pos[0] + 0.5, pos[1] + 0.5))
    print(master.piecechoice)


def cyclepiecesleft():
    if master.piecechoice - 1 < 0:
        master.piecechoice = master.settings.pieceamount - 1
    else:
        master.piecechoice -= 1

    pos = master.players[master.playerchoice].playerPieces[master.piecechoice].position
    Renderer().highlight((pos[0] + 0.5, pos[1] + 0.5))
    print(master.piecechoice)


def printspace():
    print("Space")


def cycleplayers():
    if master.playerchoice + 1 > master.settings.playeramount - 1:
        master.playerchoice = 0
    else:
        master.playerchoice += 1


def inputhandler(key):
    if master.inmenu is False:
        match key:
            case "Left":
                cyclepiecesleft()
            case "Right":
                cyclepiecesright()
            case "Return":
                cycleplayers()
            case "Space":
                printspace()

        Renderer().refreshui(master.playingfield.canvassize[0],
                             master.settings.playernames[master.playerchoice],
                             master.piecechoice, 0)


win.onclick(highlightpiece)

win.onkey(lambda key="Return": inputhandler(key), "Return")
win.onkey(lambda key="Space": inputhandler(key), "space")
win.onkey(lambda key="Left": inputhandler(key), "Left")
win.onkey(lambda key="Right": inputhandler(key), "Right")

master = GameMaster(4, 4, 3)
master.inmenu = False
win.listen()
win.mainloop()
