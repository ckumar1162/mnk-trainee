from turtle import Turtle, Screen
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title('Pong')
screen.tracer(0)
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.width(20)
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *=-1
        self.ball_speed *= 0.9
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def  reset_position(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()


class Scorboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-230, 250)
        self.write("player A :",font=("Curier", 20,"normal"))
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Courier", 20, "normal"))
        self.goto(100, 250)
        self.write("player B :", font=("Curier", 20, "normal"))
        self.goto(230, 250)
        self.write(self.r_score, align="center", font=("Courier", 20, "normal"))
    def  l_point(self):
        self.l_score += 1
        self.update()
    def r_point(self):
        self.r_score += 1
        self.update()
ball = Ball()

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350, 0))
score = Scorboard()

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"f")
screen.onkey(left_paddle.go_down,"v")


game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() < -400:
        score.r_point()
        ball.reset_position()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.xcor() > 400:
        score.l_point()
        ball.reset_position()
screen.exitonclick()
