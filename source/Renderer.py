import turtle as t
from offsetfunc import *


class Renderer:
    renderingTurtle = t.Turtle()
    writingTurtle = t.Turtle()
    clickselectTurtle = t.Turtle()

    renderingTurtle.hideturtle()
    writingTurtle.hideturtle()
    clickselectTurtle.hideturtle()

    # Draws a dot on the given coordinate with the given color offset by 0.5 on both axis
    # this resutls in the dot being drawn at the center of the coordinate.
    def render(self, color, inputtuple, dotsize, symbol):

        self.renderingTurtle.penup()
        self.renderingTurtle.hideturtle()
        self.renderingTurtle.speed(6)
        self.renderingTurtle.setpos(offsettocenter(inputtuple))
        self.renderingTurtle.width(dotsize / 12)

        if symbol == "plus":
            self.renderingTurtle.width(dotsize / 12)
            self.renderingTurtle.color(color)
            self.renderingTurtle.pendown()
            for i in range(4):
                self.renderingTurtle.forward(0.2)
                self.renderingTurtle.backward(0.2)
                self.renderingTurtle.right(90)
            self.renderingTurtle.penup()
            return

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

    def inithighlight(self, dotsize):
        self.clickselectTurtle.shape("circle")
        self.clickselectTurtle.color("orange")
        self.clickselectTurtle.hideturtle()
        self.clickselectTurtle.penup()
        self.clickselectTurtle.turtlesize(dotsize / 17)

    def highlight(self, position):
        t.tracer(False)
        self.clickselectTurtle.showturtle()
        self.clickselectTurtle.goto(position)
        t.tracer(True)

    def hidehighlight(self):
        self.clickselectTurtle.hideturtle()

    def refreshui(self, canvassize, playername, piecechosen, roll, fontsize, namelist, statetext):
        t.tracer(False)
        font = ('Arial', fontsize, 'normal')
        namefont = ('Arial', fontsize, 'bold')

        self.writingTurtle.clear()
        self.writingTurtle.hideturtle()
        self.writingTurtle.up()

        self.writingTurtle.goto(canvassize - 1 - 0.37, canvassize - 1 + 0.25)
        self.writingTurtle.color("black")
        self.writingTurtle.write(namelist[0], False, "right", namefont)
        self.writingTurtle.goto(1 + 0.37, 0 + 0.25)
        self.writingTurtle.write(namelist[1], False, "left", namefont)
        self.writingTurtle.goto(canvassize - 1 - 0.37, 0 + 0.25)
        self.writingTurtle.write(namelist[2], False, "right", namefont)
        self.writingTurtle.goto(1 + 0.37, canvassize - 1 + 0.25)
        self.writingTurtle.write(namelist[3], False, "left", namefont)

        self.writingTurtle.goto(canvassize / 2, 0.25)
        self.writingTurtle.write(statetext, False, "center", font)

        self.writingTurtle.goto(0, canvassize)
        self.writingTurtle.write(f"  Hrá {playername}", False, "left", font)

        self.writingTurtle.goto(canvassize / 2, canvassize)
        self.writingTurtle.write(f"Figúrka {piecechosen + 1} zvolená", False, "center", font)
        self.writingTurtle.goto(canvassize, canvassize)
        self.writingTurtle.write(f"Hodil si: {roll}  ", False, "right", font)
        t.tracer(True)
