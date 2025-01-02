# import smtplib
#
# my_email = "aishu2023work@gmail.com"
# password = "hsqw lmhr hqhe niwb"
#
# # list of email_id to send the mail
# li = ["2ushakk@gmail.com", "naveen@gmail.com"]
#
# for dest in li:
#     connection= smtplib.SMTP('smtp.gmail.com')
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     message = "Happy Birthday"
#     connection.sendmail(from_addr=my_email, to_addrs=dest, msg=message)
#     connection.close()
#
#

import smtplib

my_email = "aishu2023work@gmail.com"
password = "hsqw lmhr hqhe niwb"

to_addresses = ["2ushakk@gmail.com", "naveen.ijeri123@gmail.com"]
cc_addresses = ["tejas.vaidya1998@gmail.com"]

subject = "Happy Birthday"
body = "Wishing you a very Happy Birthday! "

recipients = to_addresses + cc_addresses

message = f"Subject: {subject}\nTo: {', '.join(to_addresses)}\nCc: {', '.join(cc_addresses)}\n\n{body}"

try:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipients,
            msg=message
        )
    print(f"Email successfully sent to {', '.join(to_addresses)} with CC: {', '.join(cc_addresses)}")
except Exception as e:
    print(f"An error occurred: {e}")

