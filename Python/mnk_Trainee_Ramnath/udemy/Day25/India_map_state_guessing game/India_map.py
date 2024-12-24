import turtle
from turtle import Turtle
import pandas


screen=turtle.Screen()
screen.title("India Map")
image='india_color_map.gif'
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv('india_state_names')
all_states=data['state'].to_list()
# print(all_states)
screen.tracer(0)


# coordinates = dict(zip(data['x'], data['y']))
# print(coordinates)


india_states=[]

def check_state(x,y):

    # ask user to guess state
    guess_state = screen.textinput(title="Guess State",
                                   prompt="Guess the state?").title()

    # check user guessed states are in csv file, if not then tell user to guess again
    if guess_state not in all_states :
        guess_state = screen.textinput(title="Guess again",
                                       prompt="Guess the state?").title()


    statue_value = data[data.state == guess_state]

    # checking coordinates of states click on screen is correct or not

    if abs(x -statue_value.x.item() ) < 50 and abs(y - statue_value.y.item()) < 50 and guess_state in all_states:

                  t=Turtle()
                  t.penup()
                  t.hideturtle()
                  statue_value=data[data.state==guess_state]
                  t.goto(statue_value.x.item(), statue_value.y.item())
                  t.write(guess_state)

    else:
        guess_state = screen.textinput(title="Guess again",
                                       prompt="Guess the state?").title()



screen.onclick(check_state)

screen.mainloop()
