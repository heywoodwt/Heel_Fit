# using beautifulsoup to download the html then repeat 20 seconds later and compare the old and new html if any changes are found then print a message

import requests
import os
from bs4 import BeautifulSoup
import time
import logging

url = "https://fletchertydings.com/"  # change this to the URL you want to monitor
time = 15  # seconds


def process_html(string):
    soup = BeautifulSoup(string, features="lxml")

    # make the html look good
    soup.prettify()

    # remove script tags
    for s in soup.select('script'):
        s.extract()

    # remove meta tags
    for s in soup.select('meta'):
        s.extract()

    # convert to a string, remove '\r', and return
    return str(soup).replace('\r', '')

def webpage_was_changed():
    """Returns true if the webpage was changed, otherwise false."""
    #headers = {
        #'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        #'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}
    #response = requests.get(URL_TO_MONITOR, headers=headers)
    response = requests.get(url)

    # create the previous_content.txt if it doesn't exist
    if not os.path.exists("previous_content.txt"):
        open("previous_content.txt", 'w+').close()

    filehandle = open("previous_content.txt", 'r')
    previous_response_html = filehandle.read()
    filehandle.close()

    processed_response_html = process_html(response.text)

    if processed_response_html != previous_response_html:
        filehandle = open("previous_content.txt", 'w')
        filehandle.write(processed_response_html)
        filehandle.close()
        return True
    else:
        return False

process_html(url)