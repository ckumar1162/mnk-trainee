import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server
sender_email = 'aishu2023work@gmail.com'
sender_password = 'hsqw lmhr hqhe niwb'

to_recipients = ['2ushakk@gmail.com', 'naveen.ijeri123@gmail.com']
cc_recipients = ['tejas.vaidya1998@gmail.com']

# Fetch 5 quotes from the API
api_url = "https://api.kanye.rest"
quotes = []
for _ in range(5):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        quotes.append(response.json().get("quote"))
    except Exception as e:
        print(f"Failed to fetch quote: {e}")
        quotes.append("Failed to fetch quote.")

# Format the quotes
formatted_quotes = "\n\n".join([f"{i+1}. {quote}" for i, quote in enumerate(quotes)])

#content
subject = "Inspirational Quotes from Kanye West"
body = f"""Hello,

Here are 5 quotes for you:

{formatted_quotes}

Best regards,
Usha
"""

# Create a MIME message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = ', '.join(to_recipients)
message['Cc'] = ', '.join(cc_recipients)
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Combine all recipients for sending
all_recipients = to_recipients + cc_recipients

try:
    # Connect to SMTP server and send the email
    with smtplib.SMTP(smtp_server) as server:
        server.starttls()  # Start TLS for security
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, all_recipients, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
