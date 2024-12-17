from turtle import Turtle
START_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP =90
DOWN = 270
LEFT = 180
RIGHT = 0

class SnakeGame:

    def __init__(self):
        self.segments =[]
        self.create_snake()
        

    def create_snake(self):
        #create a snake
        for my_snake in START_POS:
            self.add_segments(my_snake)

             

    def add_segments(self,my_snake):
        my_turtle = Turtle(shape = "circle")
        my_turtle.penup()
        my_turtle.goto(my_snake) #position of the turtle object
        self.segments.append(my_turtle)

    def extend(self):
        #add new segments 
        self.add_segments(self.segments[-1].position())   

    def move_snake(self):
        for snake in range(len(self.segments)-1,0,-1):
            new_x = self.segments[snake - 1].xcor()
            new_y = self.segments[snake - 1].ycor()
            self.segments[snake].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE) 
           


    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP) 

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)          

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)  

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)  