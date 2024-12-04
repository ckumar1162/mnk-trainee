import datetime as d

now =d.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

values=input("enter numbers with comma seperated")

l=values.split(",")
li=list(l)
t=tuple(li)
print(li)
print(t)

# Write a Python program that accepts a filename from the user
# and prints the extension of the file.

fname=input("enter the file name")
fn=fname.split(".")
print(fn[-1])

# Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print(color_list)

print(f"{color_list[0]} {color_list[-1]} ")
print("%s %s" % (color_list[0], color_list[-1]))

s_date=(11,12,2024)
print("{}/{}/{}".format(s_date[0],s_date[1],s_date[2]))
print("the exam will start from: %i/%i/%i"%s_date)

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5 (n+nn+nnn or 5+55+555)
# Expected Result : 615

n=int(input("enter the number"))

n1=int("%i"%n)
n2=int("%i%i"%(n,n))
n3=int("%i%i%i"%(n,n,n))

print(n1+n2+n3)

print(len.__doc__)

# 12. Write a Python program that prints the calendar for a given month and year.
import calendar

m=int(input("enter the month"))
y=int(input("enter the year"))

print(calendar.month(y,m))

# 13. Write a  Python program to print the following 'here document'.
#
# Sample string:
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

s='''A string that you "don't" have to escape
This 
is a .........multi-line
heredoc string --------> example
'''
print(s)

# Write a  Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
from datetime import date
f_date=date(2024,5,12)
l_date=date(2024,5,20)

dates=l_date-f_date
print(dates)