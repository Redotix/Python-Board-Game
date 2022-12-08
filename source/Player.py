import turtle as t
from offsetfunc import *


class Player:
    startCoords = []
    houseCoords = []
    playerColor = None
    startID = None
    endID = None
    playerPieces = []
    pieceColor = None

    def __init__(self, color, inputhouse, inputstart, startid, endid, piececolor):
        self.playerColor = color
        self.houseCoords = inputhouse
        self.startCoords = inputstart
        self.startID = startid
        self.endID = endid
        self.pieceColor = piececolor
        self.playerPieces = []

    def definepieces(self, amountofpieces):
        for i in range(amountofpieces):
            piece = self.Piece(self.pieceColor)
            self.playerPieces.append(piece)

    class Piece:
        position = None
        uniqueTurt = None

        def __init__(self, piececolor):
            self.uniqueTurt = t.Turtle()

            self.uniqueTurt.shape("circle")
            self.uniqueTurt.color(piececolor)
            self.uniqueTurt.turtlesize(1.5, 1.5)
            self.uniqueTurt.penup()

        def placepiece(self, position):
            self.uniqueTurt.speed(0)
            self.uniqueTurt.setpos(offsettocenter(position))
            self.uniqueTurt.speed(3)
            self.position = position

        # Moves the piece to the input coordinate tuple.
        def movepiece(self, coords):
            self.uniqueTurt.setpos(offsettocenter(coords))
