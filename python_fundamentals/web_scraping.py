import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((HOST,PORT))

mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    count = count + len(data)
    print(len(data), count)
    picture += data

mysock.close()

# Look for the end of the Header (2 CRLF)

pos = picture.find(b"\r\n\r\n")
print('Header Length',pos)
print(picture[:pos].decode())

# skip pass the picture and save the picture data

picture = picture[pos+4:]
fhand = open("stuff.jpg","wb")
fhand.write(picture)
fhand.close()