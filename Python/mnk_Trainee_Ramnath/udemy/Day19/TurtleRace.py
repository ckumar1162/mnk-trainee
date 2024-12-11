import random
from turtle import Turtle,Screen


is_race_on=False
s=Screen()
s.setup(height=400,width=500)
user_bet=s.textinput(title="Turtle Race",prompt="Which turtle will win. Enter color?")
color=["red","yellow","green","blue","purple"]
y_position=[-60,-30,0,30,60,90,]
all_turtle=[]


for i in range(5):
    t=Turtle(shape="turtle")
    t.penup()
    t.color(color[i])
    t.goto(x=-230,y=y_position[i])
    all_turtle.append(t)

if user_bet in color:
    is_race_on=True
else:
    print("your chosen color is not there..run again ")
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() >210:
            is_race_on=False
            winner = turtle.pencolor()
            if winner==user_bet:
                print(f"you win . The {winner} is winner.. ")
            else:
                print(f"you lose. The {winner} is winner")



        turtle_distance=random.randint(1,10)
        turtle.forward(turtle_distance)



s.exitonclick()