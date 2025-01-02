#U.S States game
import turtle as t
import pandas as pd

screen = t.Screen()
image = (r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day-25-us-states-game-start\blank_states_img.gif")
screen.title("U.S state game")
screen.addshape(image)
t.shape(image)

#read the csv file and storing the states in the list
states = pd.read_csv(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day-25-us-states-game-start\50_states.csv")
state_list = states.state.to_list()
guessed_state =[]
score = 0 
user_name =screen.textinput("User details","Enter your name ?")



# user = pd.DataFrame(userlist)
# user.to_csv(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day-25-us-states-game-start\userdetails.csv",mode = 'a' , header = False,index =False)



while len(guessed_state) < 50:
    answer = screen.textinput(f"{len(guessed_state)}/50 states are correct","enter the state name").title()
    if answer == "Exit":
        missing_state = []
        for i in state_list:
            if i not in guessed_state:
                missing_state.append(i)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("missing_data.csv")    
        break

    if answer in state_list and answer not in guessed_state:
        guessed_state.append(answer)
        score +=1
        new = t.Turtle()
        new.hideturtle()
        new.penup()
        state_data = states[states.state == answer]
        new.goto(state_data.x.item(),state_data.y.item())
        new.write(answer)

#saving user details in csv file
userlist = [{"Name":user_name,"Score":score}]
user = pd.DataFrame(userlist)
user.to_csv(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day-25-us-states-game-start\userdetails.csv",mode = 'a' , header = False,index =False)

screen.exitonclick()
