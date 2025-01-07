import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email(to_gmail, cc_gmail, body, file):
    server = 'smtp.gmail.com'
    port = 587

    sender = 'kavi02k25@gmail.com'
    password = 'ikcu rgty djop idju'
    from_person = 'kaviyarasan'
    subject = 'attached the txt file'

    message = MIMEMultipart()
    message['From'] = from_person
    message['To'] = to_gmail
    message['Cc'] = cc_gmail
    message['Subject'] = subject

    message.attach(MIMEText(body, 'html'))

    file1 = os.path.basename(file)

    with open(file1, 'rb') as file2:
        message.attach(MIMEApplication(file2.read(), _subtype="octet-stream",
                                       filename=file1))
#     message = f"""From: {from_person} <{sender}>
# To: {to_gmail}
# Cc: {cc_gmail}
# MIME-Version: 1.0
# Content-Type: text/html
# Subject: {subject}
# Hi Team,<br><br>
# i have completed the smtp sending mail part <br><br>
# {body}
# """
    recipients = [to_gmail] + [cc_gmail]

    smtpobj = smtplib.SMTP(server, int(port))
    smtpobj.starttls()
    smtpobj.login(sender, password)
    smtpobj.sendmail(sender, recipients, message.as_string())
    print("mail sent successfully")
    smtpobj.quit()


to_gmails =  "tejas.vaidya1998@gmail.com"
cc_gmails =  "naveen.ijeri123@gmail.com"
body = ("hi team, "
        "i have attached the txt file send_mail.py program  here kindly check it"
        "Thank you")
file = "send_gmail.py"


send_email(to_gmails, cc_gmails, body,file)
