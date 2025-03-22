import socket
import threading


# Creating Server

# threading what essentially means to create many threads within one python program.
PORT = 5050
HEADER = 64 # 64 bytes
SERVER = socket.gethostbyname(socket.gethostname()) # # this code equals to -> SERVER = "192.168.1.12" -> will get the local IP address.

ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# print(SERVER)

# Now after getting the IP address and the port where we want to run our server, we need to create a socket through which other devices can connect to our Server.

# first we need to bind the socket to the IP address,port to the socket.

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# socket.SOCK_STREAM -> means we are streaming data through the socket. 

# Now we need to bind this socket to the address.
server.bind(ADDR) # it means socket is bind to this address.


# setting up socket for listening, and wait for new connections.

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[DISCONNECTED] {addr} disconnected.")
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    
    conn.close()

def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[Active Connections] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()