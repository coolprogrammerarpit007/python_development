# Extract the HTML LINKS 

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import sys

count = int(input("Enter Count: "))
position = int(input("Enter Position: "))

# Ignore the ssl certificates

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter url: ")

while count > 0:
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href',None)
    count = count - 1
    continue











