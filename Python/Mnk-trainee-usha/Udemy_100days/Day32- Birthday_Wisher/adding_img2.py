import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

my_email = "aishu2023work@gmail.com"
password = "hsqw lmhr hqhe niwb"

to_addresses = ["2ushakk@gmail.com", "naveen.ijeri123@gmail.com"]
cc_addresses = ["tejas.vaidya1998@gmail.com"]

subject = "Happy Birthday "
body = "Wishing you a very Happy Birthday \n\nBest Regards"

image_path = "download.jpeg"

# Construct the email
msg = MIMEMultipart()
msg["From"] = my_email
msg["To"] = ", ".join(to_addresses)
msg["Cc"] = ", ".join(cc_addresses)
msg["Subject"] = subject

# Attach the email body
msg.attach(MIMEText(body, "plain"))

# Attach the image
try:
    with open(image_path, "rb") as attachment:
        mime_base = MIMEBase("application", "octet-stream")
        mime_base.set_payload(attachment.read())
        encoders.encode_base64(mime_base)
        mime_base.add_header("Content-Disposition", f"attachment; filename={image_path}")
        msg.attach(mime_base)
except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found. The email will be sent without the image.")

recipients = to_addresses + cc_addresses

try:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipients,
            msg=msg.as_string(),
        )
    print(f"Email successfully sent to {', '.join(to_addresses)} with CC: {', '.join(cc_addresses)}")
except Exception as e:
    print(f"An error occurred: {e}")
