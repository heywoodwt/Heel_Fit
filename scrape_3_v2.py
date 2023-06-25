import requests
import logging
from bs4 import BeautifulSoup
import time
from twilio.rest import Client

# Twilio account details
account_sid = "ACCOUNT SID"
auth_token = "AUTH TOKEN"
client = Client(account_sid, auth_token)

# Phone numbers
from_number = '+10000000000'  # Twilio number
to_number = '+10000000000'  # My number (1 for US)

url = 'https://stayactive.unc.edu/Program/GetProgramDetails?courseId=c4fca5f6-4090-48c4-aab4-8f96e4e2f9ec&semesterId=3e42e4c2-088f-469a-8ee7-755849351920'
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
    time.sleep(20)  # Wait 20 seconds before checking again
