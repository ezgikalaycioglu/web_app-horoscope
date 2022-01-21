from email.mime.text import MIMEText
import smtplib

from dotenv import load_dotenv
load_dotenv()
import os
PASSWORD=os.getenv("PASSWORD")

def send_email(email, sign, stone):
    from_email="ezgi@ezgidevelops.com"
    from_password=PASSWORD
    to_email=email

    subject="Horoscope"
    message="Hey there, your zodiac sign is <strong> %s</strong>. Your gemstone associated with your zodiac sign is <strong> %s</strong>" %(sign, stone)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtpout.secureserver.net',25)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
