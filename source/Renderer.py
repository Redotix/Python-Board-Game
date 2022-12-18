import turtle as t
from offsetfunc import *


class Renderer:
    renderingTurtle = t.Turtle()

    # Draws a dot on the given coordinate with the given color offset by 0.5 on both axis
    # this resutls in the dot being drawn at the center of the coordinate.
    def render(self, color, inputtuple, dotsize, symbol):
        self.renderingTurtle.penup()
        self.renderingTurtle.hideturtle()
        self.renderingTurtle.speed(6)
        self.renderingTurtle.setpos(offsettocenter(inputtuple))
        self.renderingTurtle.width(dotsize / 12)

        self.renderingTurtle.color("black")
        self.renderingTurtle.dot(dotsize + (dotsize / 6))
        self.renderingTurtle.color(color)
        self.renderingTurtle.dot(dotsize)

        if symbol == "star":
            self.renderingTurtle.color("black")
            self.renderingTurtle.pendown()
            for i in range(6):
                self.renderingTurtle.forward(0.2)
                self.renderingTurtle.backward(0.2)
                self.renderingTurtle.right(60)
            self.renderingTurtle.penup()

        if symbol == "questionmark":
            self.renderingTurtle.color("black")
            self.renderingTurtle.right(-90)
            self.renderingTurtle.backward(0.22)
            self.renderingTurtle.dot(dotsize / 10)
            self.renderingTurtle.forward(0.1)
            self.renderingTurtle.pendown()
            self.renderingTurtle.forward(0.1)
            self.renderingTurtle.right(45)
            self.renderingTurtle.forward(0.1)
            self.renderingTurtle.right(-22.5)
            self.renderingTurtle.forward(0.1)
            self.renderingTurtle.right(-45)
            self.renderingTurtle.forward(0.1)
            self.renderingTurtle.right(-45)
            self.renderingTurtle.forward(0.1)
            self.renderingTurtle.right(-45)
            self.renderingTurtle.forward(0.1)
            self.renderingTurtle.right(-45)
            self.renderingTurtle.forward(0.1)
            self.renderingTurtle.setheading(0)
            self.renderingTurtle.penup()
