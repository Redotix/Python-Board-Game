from Piece import *


class Player:
    playerPieces = []
    pieceColor = None
    houseColor = None
    startTileColor = None

    def __init__(self, piececolor, housecolor, starttilecolor, playeramount, piecesize):
        self.playerPieces = []
        self.pieceColor = piececolor
        self.houseColor = housecolor
        self.startTileColor = starttilecolor
        for i in range(playeramount):
            piece = Piece(self.pieceColor, piecesize)
            self.playerPieces.append(piece)
