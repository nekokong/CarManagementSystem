# 1-car-system-out.py

import socket
import csv
import uuid

###############CSV################
def writetocsv(data):
    # data = ['toyota', 'red', '1A11', '1011', '2022-05-07 15:29:15']
    with open('2-car-system-in.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data) # no 's' is single line append = row not rows
    print('csv saved')
    
#############ADDRESS##############
serverip = '192.168.1.108'
port = 8000
buffsize = 4096

# Berkeley sockets API (socket, bind, listen, accept, connect, connect_ex, send, recv, close)
#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Default IPv4

car_dict = {}

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
    
    source = data.split('|')[0] # มาจากโปรแกรมฝั่งไหน? in / location / check
    
    if source == 'in':    
        key = str(uuid.uuid1()).split('-')[0]
        car_dict[key] = data.split('|')
        # บันทึกข้อมูลที่ได้รับจาก [2] ลง csv
        # write to csv
        writetocsv(data.split('|'))
        client.send('saved'.encode('utf-8'))
        client.close()
    elif source == 'location':
        text = 'out|'
        for k,v in car_dict.items():
            text += k + '|'
            for dt in v:
                text += dt + '|'
        
        print('Send to Location: ', text)
        client.send(text.encode('utf-8'))
        client.close()
    else:
        pass
                
        








'''
1-car-system-out.py (server)
    - server.py
    function
        - บันทึกเวลาออก car-out
        - คำนวณชั่วโมงจอด
        - คำนวณค่าจอด
        - บันทึกข้อมูลที่ได้รับจาก [2]
'''