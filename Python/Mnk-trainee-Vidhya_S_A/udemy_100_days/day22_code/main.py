#pong game
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

#setting up te screen
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

#creating objects for all the class
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score = Score()

  
#event listeners
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"g")
screen.onkey(l_paddle.down,"v")



game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect paddle missess
    if ball.xcor() >380:
        ball.reset_ball()
        score.l_player_score()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_player_score()    
screen.exitonclick()