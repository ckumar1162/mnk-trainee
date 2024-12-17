import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.refresh()


    def refresh(self):
        food_x=random.randint(-280,280)
        food_y=random.randint(-280,280)
        self.goto(food_x,food_y)



