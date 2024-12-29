import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Enter a state's name:").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # print(missing_states)
        for i in missing_states:
            print(i,end=", ")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_info = data[data["state"] == answer_state]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(state_info["x"].item(), state_info["y"].item())
        state_name.write(answer_state)
