from twilio.rest import Client
from dotenv import DotEnv
dotenv = DotEnv()

TWILIO_SID = dotenv.get('TWILIO_SID')
TWILIO_AUTH_TOKEN = dotenv.get('TWILIO_TOKEN')
TWILIO_VIRTUAL_NUMBER = dotenv.get('TWILIO_SEND_NUM')
TWILIO_VERIFIED_NUMBER = dotenv.get('TWILIO_REC_NUM')


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)