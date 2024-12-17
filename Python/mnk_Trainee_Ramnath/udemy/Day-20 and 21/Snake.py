from turtle import Turtle

TURTLE_POSITION=[(0,0),(-10,0),(-30,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for i in TURTLE_POSITION:
            self.add_segment(i)

    def add_segment(self,position):
        s1 = Turtle(shape="square")
        s1.color("white")
        s1.penup()
        s1.goto(position)
        self.segment.append(s1)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)

        self.segment[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() !=LEFT:
             self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() !=RIGHT:
             self.head.setheading(LEFT)

