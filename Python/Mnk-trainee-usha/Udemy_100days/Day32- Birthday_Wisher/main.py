#sending email using python
import smtplib
my_email="aishu2023work@gmail.com"
password="hsqw lmhr hqhe niwb"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr="my_email" ,
                    to_addrs="traishwarya487@gmail.com",
                    msg="subject:Hi\n\n Good morning")
connection.close()