# from turtle import Turtle,Screen
# tummy=Turtle()
# print(tummy)
# tummy.shape("turtle")
# tummy.color("coral")
# tummy.forward(100)
#
# myscreen=Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Series",["Naruto","Inspecot Rishi","From"])
table.add_column("Language",["Japanese","Hindi","English"])
table.align="l"
print(table)
