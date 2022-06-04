# 4-car-system-check.py

import socket
from datetime import datetime

###############CSV################
import csv
def writetocsv(data):
    # data = ['toyota', 'red', '1A11', '1011', '2022-05-07 15:29:15']
    with open('2-car-system-in.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data) # no 's' is single line append = row not rows
    print('csv saved')

#############ADDRESS##############
#serverip = '159.65.135.242' # (test server uncleengineer)
serverip = '192.168.1.108' # IP of 3-car-system-location.py
port = 8500
buffsize = 4096 # Total character can receive per time

while True:
    
    text = 'check|'
    q = input('Enter Plate No. : ')
    text += q
    
    # Connect and Send (increase speed of sending)
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # function for reuse port (python socket)
    server.connect((serverip,port)) # connect() + (serverip,port)
    server.send(text.encode('utf-8'))
    data_server = server.recv(buffsize).decode('utf-8')
    print('Data from server: ', data_server)
    server.close()
    print('----------------------')
    
    
    '''
    4-car-system-check.py
    - client-3.py (connect server-location)
    function
        - ดึงข้อมูลรถ ยี่ห้อสี ป้ายทะเบียน บัตรจาก [3]
        - ดึงข้อมูลตำแหน่งโซนของรถจาก [3]
    '''