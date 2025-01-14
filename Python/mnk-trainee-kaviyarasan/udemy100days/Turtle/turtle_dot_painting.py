import turtle as t
import random

t.colormode(255)
artist = t.Turtle()
artist.speed("fast")
artist.penup()
artist.hideturtle()

colors = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124),
    (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86),
    (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158),
    (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
    (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
    (174, 94, 97), (176, 192, 209)
]

artist.setheading(225)
artist.forward(300)
artist.setheading(0)

dots = 100

for count in range(1, dots + 1):
    artist.dot(20, random.choice(colors))
    artist.forward(50)

    if count % 10 == 0:
        artist.setheading(90)
        artist.forward(50)
        artist.setheading(180)
        artist.forward(500)
        artist.setheading(0)

screen = t.Screen()
screen.exitonclick()
