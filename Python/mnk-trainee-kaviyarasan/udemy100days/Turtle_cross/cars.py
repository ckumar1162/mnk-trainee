from turtle import Turtle
import random
import turtle

class Car:
    COLORS = [
        "red", "orange", "yellow", "green", "blue", "purple",
        "pink", "cyan", "magenta", "lime", "teal", "brown",
        "gold", "silver", "navy", "maroon", "violet", "indigo",
        "olive", "coral", "turquoise"
    ]
    CARS = ["🚓", "🚗", "🏎", "🚘", "🚔"]

    def __init__(self, screen):
        self.all_cars = []
        self.car_speed = 5
        self.screen = screen

    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle(visible=False)
            car.penup()
            car.goto(random.randint(-350, 350), -280)
            car.color(random.choice(self.COLORS))
            emoji = random.choice(self.CARS)
            car.write(emoji, align="center", font=("Arial", 25, "normal"))
            self.all_cars.append((car, emoji))

    def move_cars(self):
        for car, emoji in self.all_cars:
            car.clear()
            car.sety(car.ycor() + self.car_speed)
            car.write(emoji, align="center", font=("Arial", 25, "normal"))

    def level_up(self):
        self.car_speed += 2
