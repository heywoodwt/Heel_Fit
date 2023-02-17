import requests
from bs4 import BeautifulSoup
import time

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
    elif content != last_content:  # check if the content has changed
        with open(filename, 'wb') as f:
            f.write(content)
        last_content = content
        soup = BeautifulSoup(content, 'html.parser')
        # find elements and process them here
        print('Website has been updated!')

    time.sleep(20)  # wait 20 seconds before checking again
