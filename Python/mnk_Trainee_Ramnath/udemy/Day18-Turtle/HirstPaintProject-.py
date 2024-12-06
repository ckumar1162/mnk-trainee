# TODO: extract rgb color from image
# import colorgram
#
# rgb_colors=[]
# colors=colorgram.extract('237_001.jpg',30)
# print(colors)
#
# for color in colors:
#       r=color.rgb.r
#       g=color.rgb.g
#       b=color.rgb.b
#       nw_color=(r,g,b)
#       rgb_colors.append(nw_color)
# print(rgb_colors)
import turtle
from random import random
from turtle import Turtle,Screen
import random


turtle.colormode(255)
color_list=[(233, 233, 232), (229, 233, 230), (228, 231, 236), (234, 230, 232), (200, 141, 94), (63, 90, 147), (219, 206, 100), (116, 169, 204), (162, 52, 60), (176, 77, 52), (173, 145, 69), (77, 120, 62), (142, 188, 156), (133, 35, 42), (202, 104, 72), (197, 130, 163), (180, 103, 131), (72, 128, 190), (165, 206, 213), (70, 48, 54), (60, 59, 81), (76, 54, 47), (85, 53, 48), (222, 179, 170), (176, 188, 214), (177, 202, 185), (218, 176, 185), (89, 138, 159), (116, 142, 104), (56, 54, 68)]
t=Turtle()

t.penup()
t.speed("fastest")
t.hideturtle()

t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots=100

for i in range(1,number_of_dots +1):
    t.dot(15, random.choice(color_list))
    t.forward(50)

    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)





s=Screen()
s.exitonclick()


