from Renderer import *
from PlayField import *
from Player import *

import time

CanvasSize = (13, 13)
win = t.Screen()
win.setup(600, 600)
win.setworldcoordinates(0, CanvasSize[0], CanvasSize[1], 0)
win.bgcolor("grey")

canvas = win.getcanvas()

# Variable with the playing field color and Coordinates in Touples
playingField = PlayField("white",
                         [(7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (11, 6), (11, 7),
                          (10, 7), (9, 7), (8, 7), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (6, 11), (5, 11), (5, 10),
                          (5, 9), (5, 8), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (1, 6), (1, 5), (2, 5), (3, 5),
                          (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), ])

# Variables that define the players and their team color, ending house coordinates, starting house coordinates
# starting PlayField tile, ending PlayField tile and the color of the piece.
Player1 = Player("darkBlue", [(6, 2), (6, 3), (6, 4), (6, 5), ],
                 [(10, 1), (11, 1), (10, 2), (11, 2), ], 0, 39, "blue")
Player2 = Player("gold", [(6, 10), (6, 9), (6, 8), (6, 7), ],
                 [(1, 10), (1, 11), (2, 10), (2, 11), ], 20, 19, "yellow")
Player3 = Player("darkGreen", [(10, 6), (9, 6), (8, 6), (7, 6), ],
                 [(10, 10), (10, 11), (11, 10), (11, 11), ], 10, 9, "green")
Player4 = Player("maroon", [(2, 6), (3, 6), (4, 6), (5, 6), ],
                 [(1, 1), (1, 2), (2, 1), (2, 2), ], 30, 29, "red")

players = [Player1, Player2, Player3, Player4]

for player in range(len(players)):
    players[player].definepieces(4)
    for piece in range(len(players[player].playerPieces)):
        players[player].playerPieces[piece].placepiece(players[player].startCoords[piece])

    Renderer().render(players[player].playerColor, players[player].houseCoords + players[player].startCoords)
Renderer().render(playingField.color, playingField.playingFieldVar)

for player in range(len(players)):
    for piece in range(len(players[player].playerPieces)):
        for tile in range(len(playingField.playingFieldVar)):
            players[player].playerPieces[piece].movepiece(playingField.playingFieldVar[tile])
            time.sleep(0.01)

win.mainloop()