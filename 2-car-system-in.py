# 2-car-system-in.py

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
serverip = '192.168.1.108' # IP of 1-car-system-out.py
port = 8000
buffsize = 4096 # Total character can receive per time

while True:
    
    # บันทึกข้อมูลรถ ยี่ห้อสี ป้ายทะเบียน บัตร
    info = {'brand': {'q':'Brand: ','value':''},
            'color': {'q':'Color: ','value':''},
            'plate': {'q':'Plate: ','value':''},
            'card': {'q':'Card: ','value':''}}
    # timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # data = input('Send to Server: ')
    
    for k,v in info.items():
        d = input(v['q'])
        info[k]['value'] = d
        
    text = 'in|' # 'in|' is prefix from car-system-in
    print(info)
    
    for v in info.values():
        text += v['value'] + '|'
    
    text += timestamp
    print(text)
    
    writetocsv(text.split('|'))
    
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
2-car-system-in.py (client)
    - client-1.py (connect server-out)
    function
        - บันทึกข้อมูลรถ ยี่ห้อสี ป้ายทะเบียน บัตร
        - บันทึกเวลาเข้า
        - ส่งไปหา [1]
        - บันทึกลงใน csv เครื่องตัวเอง

# run trade คือการรันหลายตัวพร้อมกันได้
# วิธีที่ทำอยู่คือการเชื่อมต่อ server ก่อนแล้วค่อยคีย์ลงไป
# แต่เราควรที่จะทำการคีย์ให้เสร็จก่อน แล้วค่อยส่งไปที่ server
# เพราะจะได้เปิดแล้วปิดเลย ไม่ต้องค้างเอาไว้นาน
'''