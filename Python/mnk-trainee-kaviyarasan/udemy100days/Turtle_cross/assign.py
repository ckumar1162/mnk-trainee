# input : "dacsb4321"
# output: "abcds10"
# input = "dacsb4321"
# alpha = "abcdefghijklmnopqrstuvwxyz"
# str_ = ""
# num = "1234567890"
# nums = 0
# for i in input:
#     if i.isalpha():
#         str_ += i
#     if i.isnumeric():
#         nums += int(i)
# output = "".join(sorted(str_)) + str(nums)
# print(output)

# list1 = sorted([ x  for x in input if x.isalpha()])
# list2 = sum([int(x) for x in input if x.isnumeric()])
# print("".join(list1) + str(list2))

# write python function move all the zeros in an integer to the End, input: 102030405, output:12345
from turtle import Screen,Turtle
import random


screen = Screen()




# a = screen.getshapes()
# print(a)


# def create_car(self):
#     screen.register_shape("turtle_car.gif.gif")
#     if random.randint(1, 6) == 1:
#         car = Turtle("turtle_car.gif.gif")
#         # self.screen.setup(width=5, height=5)
#         car.shapesize(stretch_wid=1, stretch_len=2)
#         car.penup()
#         # car.color(random.choice(self.COLORS))
#         car.goto(random.randint(-350, 350), -280)
#
#         self.all_cars.append(car)
# create_car()
#

# def create_car(self):
#     if random.randint(1, 6) == 1:
#         car = Turtle("square")  # Example for default square shape
#         car.shapesize(stretch_wid=1, stretch_len=2)  # Adjust width and length
#         car.penup()
#         car.color(random.choice(self.COLORS))
#         car.goto(random.randint(-350, 350), -280)
#         self.all_cars.append(car)

screen.register_shape("turtle_car.gif.gif")

car = Turtle("turtle_car.gif.gif")  # Example for default square shape
car.shapesize(stretch_wid=0.9, stretch_len=0.9)  # Adjust width and length
screen.setup(width=5, height=5)
car.penup()
# car.color(random.choice(self.COLORS))
car.goto(-10, 10)
screen.exitonclick()