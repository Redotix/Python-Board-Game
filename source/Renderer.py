import turtle as t
from offsetfunc import *


class Renderer:
    renderingTurtle = t.Turtle()

    # Draws a dot on the given coordinate with the given color offset by 0.5 on both axis
    # this resutls in the dot being drawn at the center of the coordinate.
    def render(self, color, inputtuple, dotsize):
        self.renderingTurtle.penup()
        self.renderingTurtle.hideturtle()
        self.renderingTurtle.speed(0)
        self.renderingTurtle.color(color)
        self.renderingTurtle.setpos(offsettocenter(inputtuple))
        self.renderingTurtle.dot(dotsize)