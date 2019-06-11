import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#setting url
url='https://en.wikipedia.org/wiki/Deep_learning'


#connect to url
response=requests.get(url)

#parse html and save it to soup object
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)

#print(soup.find_all('a'))
for links in soup.find_all('a'):
    print(links)

#printing href
for links in soup.find_all('a'):
    print(links.get('href'))