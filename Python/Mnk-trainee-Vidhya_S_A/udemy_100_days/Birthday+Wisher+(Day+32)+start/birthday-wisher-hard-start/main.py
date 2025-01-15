##################### Hard Starting Project ######################

import datetime as dt
import random
import smtplib
import pandas


my_mail='savidhya646@gmail.com'
password="mtam rzpg shcj xkia"

now=dt.datetime.now()
today_tuple=(now.month,now.day)

data=pandas.read_csv('birthdays.csv')
birth_dict={(row.month,row.day):row for (index,row) in data.iterrows()}

if today_tuple in birth_dict:
    birth=birth_dict[today_tuple]

    path_file=f"letters/letter_{random.randint(1,3)}.txt"

    with open(path_file) as letter:
        content=letter.read()
        contents=content.replace('[NAME]',birth['name'])
        print(contents)

    with smtplib.SMTP('smtp.gmail.com',port=587) as con:
        con.starttls()
        con.login(user=my_mail,password=password)
        con.sendmail(from_addr=my_mail,
                     to_addrs="tejas.vaidya1998@gmail.com",
                     msg=f'Subject:Birthday wishes\n\n {contents}')






# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



