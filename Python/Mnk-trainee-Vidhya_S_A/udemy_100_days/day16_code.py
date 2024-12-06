# #turtle module 
# import turtle

# # Create a turtle object
# pen = turtle.Turtle()

# # Set pen color and thickness
# pen.color("blue")
# pen.pensize(3)

# # Draw a square
# for _ in range(4):
#     pen.forward(100)  # Move forward by 100 units
#     pen.left(90)      # Turn left by 90 degrees

# # Keep the window open
# turtle.done()



# from turtle import Turtle,Screen
# my_object = Turtle()
# print(my_object)
# my_object.shape("turtle")
# my_object.color("red")
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


#prettytable package
from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Shinchan',['Henry','Mecssi','Shinchan','Himavari'])
table.add_column('Relation',['Father','Mother','Hero','Sister'])
table.align = "l"
print(table)