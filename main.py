from turtle import Screen
from bar import Bar, middle_line
from ball import Ball
from score import Score
import time

# editing window
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)  # disable automatic animation, to control it manually with update()

middle_line()
first_bar = Bar((370, 0))
second_bar = Bar((-370, 0))
ball = Ball()
score_one = Score((160, 210))
score_two = Score((-160, 210))

# listen to key strikes
screen.listen()
screen.onkey(fun=first_bar.move_up, key="Up")
screen.onkey(fun=first_bar.move_down, key="Down")
screen.onkey(fun=second_bar.move_up, key="w")
screen.onkey(fun=second_bar.move_down, key="s")

ball.move_right()
FORWARD_DISTANCE = 10
winner = ''
style = ("Courier", 24, "normal")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.fd(FORWARD_DISTANCE)

    # make the ball bounce
    if abs(ball.ycor()) > 285:
        ball.setheading(ball.heading() * -1)
    if ball.distance(first_bar) < 40 and ball.xcor() > 320 or ball.distance(second_bar) < 40 and ball.xcor() < -320:
        ball.setheading(180 - ball.heading())
        FORWARD_DISTANCE += 2  # increase the ball speed

    # detecting score
    if ball.xcor() < -380:
        if score_one.score < 50:
            score_one.increase_score()
            ball.home()
            ball.move_left()
            FORWARD_DISTANCE = 10
            time.sleep(1)
        else:
            winner = 'right player'
            score_one.home()
            score_one.color('yellow')
            score_one.write(f" {winner} Wins with score = {score_one.score + 10}", align='center', font=style)
            game_is_on = False

    if ball.xcor() > 380:
        if score_two.score < 50:
            score_two.increase_score()
            ball.home()
            ball.move_right()
            FORWARD_DISTANCE = 10
            time.sleep(1)
        else:
            winner = 'left player'
            score_two.home()
            score_two.color('yellow')
            score_two.write(f" {winner} Wins with score = {score_two.score + 10} ", align='center', font=style)
            game_is_on = False

screen.exitonclick()
