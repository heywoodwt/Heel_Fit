import requests
from bs4 import BeautifulSoup
import time
from twilio.rest import Client

# Twilio account details
account_sid = "AC7b2882f87de24be321f1efc9d9d8c8a5"
auth_token = "d64c8116240ac394404c7bf059adffbe"
client = Client(account_sid, auth_token)

# Website details
url = 'https://fletchertydings.com/'
filename = 'content.html'
last_content = None

# Phone numbers
from_number = '+19193715995'
to_number = '+17047800822'

while True:
    response = requests.get(url)
    content = response.content

    if last_content is None:
        # if this is the first request, save the content to a file
        with open(filename, 'wb') as f:
            f.write(content)
        last_content = content
        print('Website has been updated!')
    elif content != last_content:  # check if the content has changed
        with open(filename, 'wb') as f:
            f.write(content)
        last_content = content
        soup = BeautifulSoup(content, 'html.parser')
        # find elements and process them here
        print('Website has been updated!')

        # Send an SMS via Twilio API
        message = client.messages.create(
            body='The website has been updated!',
            from_=from_number,
            to=to_number
        )
        print('SMS sent!')

    time.sleep(20)  # wait 20 seconds before checking again
