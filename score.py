from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.write(f"score = {self.score}", align='center', font=("Courier", 30, "normal"))

    def increase_score(self):
        self.score += 10
        self.clear()
        self.write(f"score = {self.score}", align='center', font=("Courier", 30, "normal"))


