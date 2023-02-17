import requests
from bs4 import BeautifulSoup
from datetime import datetime
#from threading import Thread
import time
from twilio.rest import Client

url = "https://stayactive.unc.edu/Program/GetProgramDetails?courseId=c4fca5f6-4090-48c4-aab4-8f96e4e2f9ec&semesterId=3e42e4c2-088f-469a-8ee7-755849351920" # website to scrape
filename = 'content.html'
last_modified = None

# Twilio account details
account_sid = "AC7b2882f87de24be321f1efc9d9d8c8a5"
auth_token = "d64c8116240ac394404c7bf059adffbe"
client = Client(account_sid, auth_token)

# Phone numbers
from_number = '+19193715995' # Twilio number
#from_number = '+12223334444' # Twilio number
to_number = '+17047800822' # My number (1 for US)
#to_number = '+12223334444' # My number (1 for US)

def scrape_website():
    global last_modified
    try:
        response = requests.get(url, headers={'If-Modified-Since': last_modified})
        if response.status_code == 200:
            last_modified = response.headers.get('Last-Modified')
            content = response.content
            with open(filename, 'wb') as f:
                f.write(content)
            soup = BeautifulSoup(content, 'lxml')
            # find elements and process them here
            print('Website has been updated!')

            # Send an SMS via Twilio API
            message = client.messages.create(
                body = 'NEW HEEL FIT POSTED!',
                from_ = from_number,
                to = to_number
            )
            print('SMS sent!')
    except:
        pass

while True:
    start_time = datetime.now()
    scrape_website()
    end_time = datetime.now()
    time_diff = (end_time - start_time).total_seconds()
    sleep_time = max(20 - time_diff, 0) # wait 20 seconds before checking again
    time.sleep(sleep_time)
