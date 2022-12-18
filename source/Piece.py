import turtle as t
from offsetfunc import *


class Piece:
    position = None
    uniqueTurt = None
    currentpos = None
    isfinished = False

    def __init__(self, piececolor, piecesize):
        self.uniqueTurt = t.Turtle()

        self.uniqueTurt.shape("circle")
        self.uniqueTurt.color(piececolor)
        self.uniqueTurt.turtlesize(1.5, 1.5)
        self.uniqueTurt.penup()
        self.uniqueTurt.turtlesize(piecesize / 25)

    def placepiece(self, position):
        self.uniqueTurt.speed(0)
        self.uniqueTurt.setpos(offsettocenter(position))
        self.uniqueTurt.speed(3)
        self.position = position

    # Moves the piece to the input coordinate tuple.
    def movepiece(self, coords):
        self.uniqueTurt.setpos(offsettocenter(coords))