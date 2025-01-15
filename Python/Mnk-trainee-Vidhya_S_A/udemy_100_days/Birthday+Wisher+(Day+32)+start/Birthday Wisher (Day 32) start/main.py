import datetime as dt
import smtplib
import random

my_email = "savidhya646@gmail.com"
pw = "mtam rzpg shcj xkia"
current_day = dt.datetime.now()
weekday = current_day.weekday()
if weekday == 2:

    with open(r'mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\Birthday+Wisher+(Day+32)+start\Birthday Wisher (Day 32) start\quotes.txt') as quotes:
        data = quotes.readlines()
        quote = random.choice(data)

        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=pw)
            connection.sendmail(from_addr=my_email,to_addrs="vidhyaannadurai31@gmail.com",msg=f'Subject:Motivation\n{quote}')



















# import smtplib

# my_mail = "savidhya646@gmail.com"
# password = "mtam rzpg shcj xkia"
# connection = smtplib.SMTP('smtp.gmail.com',587)
# connection.starttls() # secure the connection
# connection.login(user=my_mail,password=password)
# connection.sendmail(from_addr=my_mail,to_addrs='vidhyaannadurai31@gmail.com',msg="Hello")
# connection.close()


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# week = now.weekday()
# print(now)
# print(year)
# print(month)
# print(week)