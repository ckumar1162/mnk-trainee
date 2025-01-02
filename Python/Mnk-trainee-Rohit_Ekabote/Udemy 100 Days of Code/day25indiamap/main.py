import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("India Map")
image = "india_color_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("india_state_names.csv")
all_states = data['state'].to_list()

score_list = pandas.read_csv("userdetails.csv")
all_score = score_list['Score'].to_list()
high_score = max(all_score)
# print(all_states)
screen.tracer(0)
score = 0
india_states = []

# user prompt
user_name = screen.textinput("User details", "Enter your name ?")


# saving user details in csv file
def save_user():
    userlist = [{"Name": user_name, "Score": score}]
    user = pandas.DataFrame(userlist)
    user.to_csv("userdetails.csv", mode='a', header=False, index=False)


def check_state(x, y):
    global score, high_score

    # ask user to guess state
    guess_state = screen.textinput(title=f"{score}/{len(all_states)} Guess State high_score ={high_score}",
                                   prompt="Guess the state?").title()
    # if user type exit then save the sore in csv
    if guess_state == "Exit":
        save_user()
        screen.bye()
        return
    # check user guessed states are in csv file, if not then tell user to guess again
    if guess_state not in all_states:
        guess_state = screen.textinput(title="Guess again high_score ={high_score}",
                                       prompt="Guess the state?").title()
        if guess_state == "Exit":
            save_user()
            screen.bye()
            return

    statue_value = data[data.state == guess_state]

    # checking coordinates of states click on screen is correct or not

    if abs(x - statue_value.x.item()) < 50 and abs(
            y - statue_value.y.item()) < 50 and guess_state in all_states and guess_state not in india_states:
        india_states.append(guess_state)
        score += 1
        if high_score < score:
            high_score = score
        t = Turtle()
        t.penup()
        t.hideturtle()
        statue_value = data[data.state == guess_state]
        t.goto(statue_value.x.item(), statue_value.y.item())
        t.write(guess_state)
    else:
        guess_state = screen.textinput(title="Guess again high_score ={high_score}",
                                       prompt="Guess the state?").title()
        if guess_state == "Exit":
            save_user()
            screen.bye()
            return


screen.onclick(check_state)

screen.mainloop()