from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(-360, 0)

    def move_front(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_back(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
