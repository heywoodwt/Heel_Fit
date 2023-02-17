from twilio.rest import Client

# Set up the Twilio client with your account SID and auth token
account_sid = "AC7b2882f87de24be321f1efc9d9d8c8a5"
auth_token = "d64c8116240ac394404c7bf059adffbe"
client = Client(account_sid, auth_token)

# Send an SMS message
message = client.messages.create(
    to='+17047800822',  # Replace with the recipient's phone number
    from_='+19193715995',  # Replace with your Twilio phone number
    body='Hello, world!'  # Replace with the message you want to send
)

# Print the message SID
print(message.sid)
