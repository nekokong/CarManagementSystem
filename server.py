# server.py

import socket

# CMD - ipconfig IP4
serverip = '192.168.1.108'
port = 8000
buffsize = 4096

# Berkeley sockets API (socket, bind, listen, accept, connect, connect_ex, send, recv, close)
#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Default IPv4

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # function for reuse port (python socket)
    server.bind((serverip, port))
    server.listen(1)
    print('waiting client...')
    
    client, addr = server.accept()
    print('connected from:', addr)
    
    data = client.recv(buffsize).decode('utf-8')
    print('Data from client: ', data)
    client.send('received your messsage.'.encode('utf-8'))
    client.close()

    