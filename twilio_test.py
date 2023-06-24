from twilio.rest import Client

# Set up the Twilio client with your account SID and auth token
account_sid = "ACCOUNT SID"
auth_token = "AUTH TOKEN"
client = Client(account_sid, auth_token)

# Send an SMS message
message = client.messages.create(
    to='+10000000000',  # Replace with the recipient's phone number
    from_='+10000000000',  # Replace with your Twilio phone number
    body='H Rules!'  # Replace with the message you want to send
)

# Print the message SID
print(message.sid)
