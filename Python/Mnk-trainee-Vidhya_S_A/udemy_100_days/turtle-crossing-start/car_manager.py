from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_car = []
        self.speed_car = STARTING_MOVE_DISTANCE

    def create_car(self):
        min_car = random.randint(1,6)
        if min_car ==6:
            my_car = Turtle("square")
            my_car.shapesize(1,2)
            my_car.penup()
            my_car.color(random.choice(COLORS))
            y_pos = random.randint(-250,250)
            my_car.goto(290,y_pos)
            self.all_car.append(my_car) 

    def move_car(self):
        for car in self.all_car:
            car.backward(self.speed_car)

    def car_speed(self):
        self.speed_car += MOVE_INCREMENT
