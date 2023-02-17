import requests
from bs4 import BeautifulSoup

# make a GET request to the website you want to scrape
url = 'https://stayactive.unc.edu/Program/GetProgramDetails?courseId=c4fca5f6-4090-48c4-aab4-8f96e4e2f9ec&semesterId=3e42e4c2-088f-469a-8ee7-755849351920'
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# find elements on the page by their HTML tags or CSS classes/ids
title = soup.find('title').text
#header = soup.find('h1', class_='header').text
#links = [link['href'] for link in soup.find_all('a')]

# print the results
print(title)
#print(header)
#print(links)

# if title changes then print a message every 20 seconds
if title != title:
    print('Website has been updated!')
else:
    print('Website has not been updated.'




