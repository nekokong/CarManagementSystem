# 3-car-system-location.py

import socket
from datetime import datetime

###############Threading Server################

plate_dict = {}
# plate_dict = {'1AB7128':['4564131','646513','4643133']}

import threading
serverip_location = '192.168.1.108'
port_location = 8500
buffsize_location = 4096

def LocationServer():
    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # function for reuse port (python socket)
        server.bind((serverip_location, port_location))
        server.listen(1)
        print('waiting client...')
        
        client, addr = server.accept()
        print('connected from:', addr)
        
        data = client.recv(buffsize_location).decode('utf-8')
        print('Data from client: ', data)
        
        # data from 4 : data = 'check|1AB7128'
        source = data.split('|')[0] # มาจากโปรแกรมฝั่งไหน? in / location / check
        plate = data.split('|')[1] # '1AB7128'
        
        if source == 'check':
            # text = '1AB7128'
            check = plate_dict[plate] # ['f583f7b5', 'in', 'toyota', 'red', '1AB7128', '1001', '2022-05-07 15:29:15']
            text = 'loction|'
            for c in check:
                text += c + '|'
                
            client.send(text.encode('utf-8'))
            client.close()
        else:
            client.close()

##########RUN THREADING###########
task = threading.Thread(target=LocationServer)
task.start()

###############CSV################
import csv
def writetocsv(data):
    # data = ['toyota', 'red', '1A11', '1011', '2022-05-07 15:29:15']
    with open('2-car-system-in.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data) # no 's' is single line append = row not rows
    print('csv saved')

###############Split################
def splitrow(datalist, columns=7):
    result = []
    buflist = []
    for i,t in enumerate(datalist,start=1):
        if i % columns == 0:
            buflist.append(t)
            # print(buflist)
            result.append(buflist)
            buflist = []
        else:
            buflist.append(t)
    return result

#############ADDRESS##############
#serverip = '159.65.135.242' # (test server uncleengineer)
serverip = '192.168.1.108'
port = 8000
buffsize = 4096 # Total character can receive per time

while True:
    q = input('[1] - get all car information\n[2] - get single car information\n[3] - Save Car Zone\n[q] - exit\n>>> ')
    if q == '1':
        text = 'location|allcar'
    elif q == '2':
        getcar = 'Enter Plate Code: '
        text = 'location|{}'.format(getcar)
    elif q == '3':
        plate = input('Enter Plate Code: ')
        getzone = input('Enter Zone Number: ')
        if len(plate_dict[plate]) == 7:
            # ถ้ายังไม่เคยกรอก ข้อมูลจะมีทั้ง 7 รายการ
            plate_dict[plate].append(getzone)
        else:
            # ถ้าเคยกรอกไปแล้ว ต้องการเปลี่ยนให้ใช้แบบนี้
            plate_dict[plate][7] = getzone
        
    elif q == 'q':
        break
    
    if q != '3':
        # Connect and Send (increase speed of sending)
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # function for reuse port (python socket)
        server.connect((serverip,port)) # connect() + (serverip,port)
        server.send(text.encode('utf-8'))
        data_server = server.recv(buffsize).decode('utf-8')
        print('Data from server: ', data_server)
        datalist = data_server.split('|')[1:-1] # remove prefix and suffix in data
        for row in splitrow(datalist, 7):
            print(row)
            # ['f583f7b5', 'in', 'toyota', 'red', '1AB7128', '1001', '2022-05-07 15:29:15']
            if row[4] not in plate_dict:
                plate_dict[row[4]] = row # บันทึกข้อมูลของรถเก็บไว้เป็น dict
        server.close()
        



'''
3-car-system-location.py
    - client-1.py (connect server-out)
        function
        - ดึงข้อมูลรถ ยี่ห้อสี ป้ายทะเบียน บัตรจาก [1]
    - server.py
        function
        - บันทึกตำแหน่งโซนที่จอดของรถได้
        - ส่งข้อมูลรถไปยัง [4]
'''