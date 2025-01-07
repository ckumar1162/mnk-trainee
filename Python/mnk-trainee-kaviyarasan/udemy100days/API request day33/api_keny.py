import requests
import smtplib
from email.message import EmailMessage

respons = requests.get(url="https://api.kanye.rest/")

data = respons.json()["quote"]

try:
    with open(r"quotes.txt","a") as file:
        file.write(data + "\n")
except FileNotFoundError:
    with open("quotes.txt","w") as file:
        file.write(data)

def send_gmail(to_gmail, cc_gmail, body, file):
    sender = 'kavi02k25@gmail.com'
    password = 'ikcu rgty djop idju'
    subject = 'Attached the txt file'

    message = EmailMessage()
    message['From'] = sender
    message['To'] = to_gmail
    message['Cc'] = cc_gmail
    message['Subject'] = subject
    message.set_content(body)

    with open(file, 'r') as file_content:
        message.add_attachment(file_content.read(),subtype='plain',filename=file)

    recipients = [to_gmail] + [cc_gmail]

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(sender, password)
    smtp.send_message(message)
    print("mail send successfully")
    smtp.quit()

to_gmail = "tejas.vaidya1998@gmail.com"
cc_gmail = "naveen.ijeri123@gmail.com"
body = """Hi team,

I have attached the quotes.txt file.
using the api request and appended the text in the file,

Thank you."""
file = "quotes.txt"

send_gmail(to_gmail, cc_gmail, body, file)