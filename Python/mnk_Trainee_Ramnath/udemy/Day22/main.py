from turtle import Screen, Turtle
import time
from Paddling import Paddling
from ball import Ball
from udemy.Day22.scoreboard import ScoreBoard

s=Screen()
s.setup(width=800,height=600)
s.bgcolor("black")
s.title("PONG GAME")
s.tracer(0)


r_paddle=Paddling((350,0))

l_paddle=Paddling((-350,0))


ball=Ball()

score=ScoreBoard()

s.listen()

s.onkey(r_paddle.move_up,'Up')
s.onkey(r_paddle.move_down,'Down')

s.onkey(l_paddle.move_down,'s')
s.onkey(l_paddle.move_up,'w')


is_game_on=True

while is_game_on:
    time.sleep(ball.speed1)
    s.update()

    ball.move()

    # Detect collision with wall and bounce back logic
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor()<-320:
        ball.bounce_x()
    # Detect Right paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        score.left_score()

    # Detect Left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        score.right_score()


s.exitonclick()
