from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()

    def move_right(self):
        self.setheading(random.randrange(-70, 70, 20))

    def move_left(self):
        self.setheading(180 + random.randrange(-70, 70, 20))

