import urllib.request, urllib.error,urllib.parse
import re
import ssl
import sys


# Once the web page has been opened with urllib.request.urlopen, we can treat it like a file and read through it using a for loop.

# When the program runs, we only see the output of the contents of the file. The headers are still sent, but the urllib code consumes the headers and only returns the data to us.
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')


counts = dict()
for line in fhand:
    line = line.decode().rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# print(counts)


#   Storing Binary Files (Video/Img ) into computer

# img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
# fhand = open('python-cover.jpg','wb')
# fhand.write(img)
# fhand.close()

# img = urllib.request.urlopen('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWppdWU3bWRpajFzYmFzNGQxdWpqc3owenRodDlpaGFjNXV5Y3I3ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/11xBk5MoWjrYoE/giphy.gif')
# fhand = open('animated-GIF.gif','wb')
# size = 0

# while True:
#     info = img.read(100000)
#     if len(info) < 1:break
#     size += len(info)
#     fhand.write(info)

# print(size,'Characters Copied!')
# fhand.close()


# Scraping URL Links 

# Ignore The SSL Certification 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter -")
html = urllib.request.urlopen(url,context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"',html)
for link in links:
    print(link.decode())

