import socket 

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('data.pr4e.org',80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
client.send(cmd)

while True:
    data = client.recv(512)
    if len(data) < 1:break
    print(data.decode(),end="")

client.close()

