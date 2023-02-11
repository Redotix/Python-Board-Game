from Piece import *


class Player:
    playerPieces = []
    pieceColor = None
    houseColor = None
    startTileColor = None

    def __init__(self, piececolor, housecolor, starttilecolor, pieceamount, piecesize):
        self.playerPieces = []
        self.pieceColor = piececolor
        self.houseColor = housecolor
        self.startTileColor = starttilecolor
        for thispiece in range(pieceamount):
            piece = Piece(self.pieceColor, piecesize, thispiece)
            self.playerPieces.append(piece)
