# import smtplib
# import base64
#
# my_email = "aishu2023work@gmail.com"
# password = "hsqw lmhr hqhe niwb"
#
# # Recipients
# to_addresses = ["2ushakk@gmail.com", "naveen@gmail.com"]
# cc_addresses = ["tejas@example.com"]
#
# # Email content
# subject = "Happy Birthday"
# body = "Wishing you a very Happy Birthday! \n\nPlease find the attached image."
#
# # Path to the image
# image_path = "download.jpeg"
#
# # Read the image file
# with open(image_path, "rb") as image_file:
#     image_data = image_file.read()
#     image_encoded = base64.b64encode(image_data).decode()
#
# # Combine all recipients (To + CC)
# recipients = to_addresses + cc_addresses
# message = f"Subject: {subject}\nTo: {', '.join(to_addresses)}\nCc: {', '.join(cc_addresses)}\n\n{body}"
#
# # Send the email
# try:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=recipients,
#             msg=message
#         )
#     print(f"Email successfully sent to {', '.join(to_addresses)} with CC: {', '.join(cc_addresses)}")
# except Exception as e:
#     print(f"An error occurred: {e}")

import smtplib
import base64

my_email = "aishu2023work@gmail.com"
password = "hsqw lmhr hqhe niwb"

# Recipients
to_addresses = ["2ushakk@gmail.com", "naveen@gmail.com"]
cc_addresses = ["tejas@example.com"]

# Email content
subject = "Happy Birthday"
body = "Wishing you a very Happy Birthday! \n\nPlease find the attached image."

# Path to the image
image_path = "download.jpeg"

# Read the image file
with open(image_path, "rb") as image_file:
    image_data = image_file.read()
    image_encoded = base64.b64encode(image_data).decode()

# Combine all recipients (To + CC)
recipients = to_addresses + cc_addresses

# Construct the email message with an attachment
boundary = "----boundary_text"
message = f"""\
Subject: {subject}
To: {', '.join(to_addresses)}
Cc: {', '.join(cc_addresses)}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="{boundary}"

--{boundary}
Content-Type: text/plain

{body}

--{boundary}
Content-Type: image/jpeg; name="{image_path}"
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="{image_path}"

{image_encoded}

--{boundary}--
"""

# Send the email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
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
