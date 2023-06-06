from turtle import Turtle


def middle_line():
    line = Turtle()
    line.color('white')
    line.hideturtle()
    line.penup()
    line.goto(0, 295)
    line.setheading(270)
    while line.ycor() != -295:
        line.pendown()
        line.fd(5)
        line.penup()
        line.fd(5)


class Bar(Turtle):
    def __init__(self, position):
        super().__init__()  # inherit Turtle attributes and methods
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        # width = 5 * 20 , height  = 1 * 20
        self.color('white')
        self.penup()
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
