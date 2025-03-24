# Using Beautiful soup library to extract numbers and find sum of it.
import bs4
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen
import re


# Ignore SSL Certifications
ctx = ssl.create_default_context()
ctx.check_hostname =False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,"html.parser")
list_numbers = []

# Retreived all of the span tags

tags = soup('span')
for tag in tags:
    tag = tag.decode()
    number = (re.findall('[0-9]+',tag))
    number = float(''.join(number))
    list_numbers.append(number)
   

print(f"Sum Of Numbers: {sum(list_numbers)}")