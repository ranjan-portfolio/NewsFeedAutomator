
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

load_dotenv()

APP_PASSWORD = os.getenv("APP_PASSWORD")

sender_list=["ranjanabha@gmail.com"]

def sendemail(response: str) -> str:

    subject="Your daily tech news byte"
    SENDER_EMAIL="ranjanabha@gmail.com"
    receiver_list=["ranjanabha@gmail.com","roy777rajat@gmail.com"]

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = ",".join(receiver_list)
        msg.attach(MIMEText(response, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_list, msg.as_string())

        return f"✅ Email sent successfully to {receiver_list}"
    except Exception as e:
        return f"❌ Failed to send email: {str(e)}"