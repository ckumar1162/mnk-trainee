from turtle import Turtle, Screen
import random
is_raceon = False
my_screen = Screen()
my_screen.setup(500,400)
user = my_screen.textinput(title="Make ur bet",prompt="Which turtle will win the race.Enter the color:")
colours = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
y_pos = [-100,-70,-40,-10,20,50,80]
all_turtles = []


for each_turtle in range(0,7):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colours[each_turtle])
    my_turtle.penup()
    my_turtle.goto(x=-230,y=y_pos[each_turtle])
    all_turtles.append(my_turtle)

if user:
    is_raceon = True

while is_raceon:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_raceon = False
            winning_colour = turtle.pencolor()
            if winning_colour == user:
                print(f"Oh yeah!! ,You won  and the winner is {winning_colour} turtle")
            else:
                print(f"Oh nooo!! ,You lost  and the winner is {winning_colour} turtle")    
        speed = random.randint(0,10)    
        turtle.forward(speed)








my_screen.exitonclick()