from twilio.rest import Client
import smtplib

TWILIO_SID = "AC619c53f20e49be7ec159c898892f0cba"
TWILIO_AUTH_TOKEN = "5576b34c3916a227a529b3de6ff123f8"
TWILIO_VIRTUAL_NUMBER = '+19034156884'
TWILIO_VERIFIED_NUMBER = '+5491158870286'

MY_EMAIL = "baalbornozl1312@gmail.com"
PASSWORD = "%(mpn42G2ISV+T4$"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        # print(message.sid)

    def send_emails(self, emails, message, link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=emails,
                msg=f"subject:ALERTA DE VUELO.\n\n{message}.\n\n{link}. "
            )
