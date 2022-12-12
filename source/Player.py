from Piece import *


class Player:
    startCoords = []
    houseCoords = []
    playerColor = None
    startID = None
    endID = None
    playerPieces = []
    pieceColor = None

    def __init__(self, color, inputhouse, inputstart, startid, endid, piececolor, pieceamount):
        self.playerColor = color
        self.houseCoords = inputhouse
        self.startCoords = inputstart
        self.startID = startid
        self.endID = endid
        self.pieceColor = piececolor
        self.playerPieces = []
        for i in range(pieceamount):
            piece = Piece(self.pieceColor)
            self.playerPieces.append(piece)

