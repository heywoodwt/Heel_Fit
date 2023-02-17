import requests
from bs4 import BeautifulSoup
import time

url = 'https://stayactive.unc.edu/Program/GetProgramDetails?courseId=c4fca5f6-4090-48c4-aab4-8f96e4e2f9ec&semesterId=3e42e4c2-088f-469a-8ee7-755849351920'
last_content = None

while True:
    response = requests.get(url)
    content = response.content

    if content != last_content:  # check if the content has changed
        last_content = content
        soup = BeautifulSoup(content, 'html.parser')
        # find elements and process them here
        print('Website has been updated!')

    time.sleep(20)  # wait 20 seconds before checking again
