import smtplib
import datetime as dt
import random
from calendar import weekday

MY_EMAIL="aishu2023work@gmail.com"
MY_PASSWORD="hsqw lmhr hqhe niwb"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:# checking for a monday
    with open("quotes.txt","r")as file:
        all_quotes=file.readlines()
        quote=random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="traishwarya487@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

#send email to multiple user
#attach image
#to -> yourself, naveen

#cc -> tejas
