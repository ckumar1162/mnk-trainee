from turtle import Turtle ,Screen
import random
t=Turtle()

WIDTH,HEIGHT=400,400
color_list=["red","green","yellow","blue","orange","purple","black","pink","brown","aquamarine1"]
def no_of_turtles():
    count=0
    while True:
        num=int(input("How many turtles you want in the race:"))
        if num>=2 and num<=10:
            return num
        else:
            print("Input is not in the range, Please try again....")
turtles=no_of_turtles()
print(turtles)#3

s=Screen()
s.setup(400,400)# width and height of a screen

x_spacing=WIDTH//(turtles+1)
turtle_list=[]
for i in range(1,turtles+1):
    #t=Turtle()
    t.shape("turtle")
    t.left(90)
    t.color(random.choice(color_list))
    t.penup()
    t.goto=(-WIDTH//2 + (i*x_spacing) ,-HEIGHT//2+10)


s.exitonclick()