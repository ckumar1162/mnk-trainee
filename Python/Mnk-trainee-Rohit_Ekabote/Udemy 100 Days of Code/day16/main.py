#import turtle
import another_module
print(another_module.another_variable)

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
timmy.backward(200)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemon name", ['pikachu', 'squirtle', 'charmander'])
table.add_column("type", ['electric', 'water', 'fire'])
print(table.align)
table.align = 'l'
print(table)

