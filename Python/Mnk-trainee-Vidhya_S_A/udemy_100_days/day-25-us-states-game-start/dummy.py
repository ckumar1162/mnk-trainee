from turtle import Screen
import pandas


screen = Screen()
new = screen.textinput("user details","enter ur name")
userlist = []
userlist.append(new)

user = pandas.DataFrame(userlist)
user.to_csv(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\day-25-us-states-game-start\userdetails.csv")


screen.exitonclick()
