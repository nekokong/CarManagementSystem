# client.py

import socket

serverip = '192.168.1.108'
port = 8000
buffsize = 4096 # Total character can receive per time

for i in range(10):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # function for reuse port (python socket)
    server.connect((serverip,port)) # connect() + (serverip,port)
    
    data = input('Send to Server: ')
    server.send(data.encode('utf-8'))
    
    data_server = server.recv(buffsize).decode('utf-8')
    print('Data from server: ', data_server)
    server.close()
    
    
