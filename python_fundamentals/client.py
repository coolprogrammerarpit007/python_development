# Socket Programming

# creating client for connecting to the server

import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

# creating client
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connecting client to the server
client.connect(ADDR) # client is now officially connected to the server.

def send(msg):
    message = msg.encode(FORMAT) # this will encode message send string into the bytecode.
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length) # this will send the length of the message to the server.
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
send("I am Arpit ")
send("I have created mylocal server so clients other local systems can connect to it. ")
send("I am a software developer from India!")
send(DISCONNECT_MESSAGE)


# CODE EXPLAINATION from line 21 to 27

# Let's break down the send function and the subsequent calls to it in simple terms:

# The send Function
# message = msg.encode(FORMAT)

# This line takes the input message (msg) and converts it into a format that computers can understand better. Think of it like translating a sentence into a language that the computer can process. The FORMAT variable likely specifies how this translation should be done (e.g., UTF-8).

# msg_length = len(message)

# Here, the function calculates the length of the translated message. This is important because the server needs to know how much data to expect.

# send_length = str(msg_length).encode(FORMAT)

# This line converts the length of the message into a string and then translates it into the same computer-friendly format as before. This is necessary because the length needs to be sent to the server first.

# send_length += b' ' * (HEADER - len(send_length))

# The server expects the message length to be a certain size (defined by HEADER). If the length is shorter than this, it pads the length with spaces until it reaches the required size. This ensures that the server always knows where the length ends.

# client.send(send_length)

# This line sends the length of the message to the server. The server uses this to know how much data to expect next.

# client.send(message)

# Now, it sends the actual message to the server.

# print(client.recv(2048).decode(FORMAT))

# After sending the message, the client waits for a response from the server. It receives up to 2048 bytes of data, translates it back into human-readable text, and prints it.