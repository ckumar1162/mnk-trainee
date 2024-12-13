import turtle
from turtle import Turtle,Screen
import pandas as pd

t=Turtle()
s=Screen()

s.title("U.S States Game")
image="blank_states_img.gif"
s.addshape(image)
t.shape(image)

df=pd.read_csv("50_states.csv")
all_states=df.state.to_list() #converting state data to list

#taking input from the user
guessed_state=[]

while len(guessed_state)<50:
    answer=s.textinput(title="Guess the state",prompt="What's the state name").title()

    if answer=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        print(missing_states)
        break
#checking if user input with data that we are having are same or not
    if answer in all_states:
        guessed_state.append(answer)
        t1=turtle.Turtle()
        t1.hideturtle()
        t1.penup()
        data=df[df.state==answer]
        t1.goto(int(data.x.iloc[0]),int(data.y.iloc[0]))
        t1.write(data.state.item())


s.exitonclick()