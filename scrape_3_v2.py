import requests
import logging
from bs4 import BeautifulSoup
import time
from twilio.rest import Client

# Twilio account details
account_sid = "AC7b2882f87de24be321f1efc9d9d8c8a5"
auth_token = "d64c8116240ac394404c7bf059adffbe"
client = Client(account_sid, auth_token)

# Phone numbers
from_number = '+19193715995'  # Twilio number
to_number = '+17047800822'  # My number (1 for US)

url = 'https://kotangorocks.z13.web.core.windows.net/'
filename = 'content.html'
last_content = None

while True:
    response = requests.get(url)
    content = response.content

    if last_content is None:
        # if this is the first request, save the content to a file
        with open(filename, 'wb') as f:
            f.write(content)
        last_content = content
        logging.info('Heel Fit Website Has Been Downloaded!')
    elif content != last_content:  # check if the content has changed
        with open(filename, 'wb') as f:
            f.write(content)
        last_content = content
        soup = BeautifulSoup(content, 'html.parser')
        # find elements and process them here
        logging.info('Heel Fit Website Has Been Updated!')

        # Send an SMS via Twilio API
        message = client.messages.create(
            body='NEW HEEL FIT POSTED!',
            from_=from_number,
            to=to_number
        )
        logging.info('Text Message Sent!')
    time.sleep(20)  # wait 20 seconds before checking again
