import turtle
from os import stat_result
from turtle import Turtle

import pandas



screen=turtle.Screen()
screen.title("U.S State Game")
image='blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data=pandas.read_csv('50_states.csv')
all_state=data['state'].to_list()

state_list=[]

while len(state_list) < 50:
    guess_state=screen.textinput(f"{len(state_list)}/50 Guess the state",prompt="What's another state name?").title()

    if guess_state =="Exit":
        missed_states=[]
        # Adding not guessed states in csv files
        for state in all_state:
            if state not in state_list:
                missed_states.append(state)
        data=pandas.DataFrame(missed_states)
        data.to_csv("states_to_learn.csv")
        break

    if guess_state in all_state:
        state_list.append(guess_state)
        t=Turtle()
        t.penup()
        t.hideturtle()
        state_value=data[data.state == guess_state]
        print(state_value)
        print(state_value.x)
        t.goto(state_value.x.item(),state_value.y.item())
        t.write(guess_state)





screen.mainloop()