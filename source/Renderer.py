import turtle as t
from offsetfunc import *


class Renderer:
    renderingTurtle = t.Turtle()

    # Draws a dot on the given coordinate with the given color offset by 0.5 on both axis
    # this resutls in the dot being drawn at the center of the coordinate.
    def render(self, color, field):
        self.renderingTurtle.penup()
        self.renderingTurtle.hideturtle()
        self.renderingTurtle.speed(0)
        t.tracer(False)
        self.renderingTurtle.color(color)
        for fieldTile in range(len(field)):
            self.renderingTurtle.setpos(offsettocenter(field[fieldTile]))
            self.renderingTurtle.dot(40)
        t.tracer(True)
