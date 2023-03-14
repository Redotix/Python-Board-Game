import turtle as t
from offsetfunc import *


class Piece:
    position = None
    uniqueTurt = None
    piecenumber = None
    positioninplayingfield = None
    positioninhouse = -1
    tilesmoved = 0
    isinhouse = False

    def __init__(self, piececolor, piecesize, piecenumber):
        self.uniqueTurt = t.Turtle()
        self.piecenumber = piecenumber
        self.uniqueTurt.shape("circle")
        self.uniqueTurt.color(piececolor)
        self.uniqueTurt.penup()
        self.uniqueTurt.turtlesize(piecesize / 25)

        # self.uniqueTurt.onclick(self.getpieceid)

    def placepiece(self, position):
        self.uniqueTurt.speed(0)
        self.uniqueTurt.setpos(offsettocenter(position))
        self.uniqueTurt.speed(3)
        self.position = position

    # Moves the piece to the input coordinate tuple.
    def movepiece(self, coords):
        self.uniqueTurt.setpos(offsettocenter(coords))
        self.position = coords
        
    # def getpieceid(self, dummy, dummy2):
    #     print(self.piecenumber, self.position)
    #     return self.position
