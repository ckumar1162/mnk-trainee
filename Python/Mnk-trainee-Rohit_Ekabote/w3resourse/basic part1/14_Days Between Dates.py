"""Write a  Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days"""

from datetime import date

print((date(2014, 7, 11)-date(2014, 7, 2)).days)

#or

f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
difference = l_date - f_date
print(difference.days)