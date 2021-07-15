import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_number = os.environ['FROM_NUMBER']
to_number = os.environ['TO_NUMBER']
msg_svc_sid = os.environ['MESSAGING_SERVICE_SID']

client = Client(account_sid, auth_token)

### Method 1 ###
# message = client.messages \
#                 .create(
#                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                     from_=from_number,
#                     to=to_number
#                 )

### Method 2 ###
message = client.messages \
                .create(
                    messaging_service_sid=msg_svc_sid,
                    body='Sent from Twilio - My first Messaging Service',
                    to=to_number
                )

print(message.sid)
