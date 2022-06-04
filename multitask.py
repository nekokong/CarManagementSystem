# multitask.py

import threading
import time

# 1. ขับรถให้เสร็จก่อนแล้วค่อยประชุม
def Driving():
    # 10 second
    for i in range(10):
        print('กำลังขับรถอยู่...', i)
        time.sleep(1)


def Meeting():
    for i in range(10):
        print('กำลังประชุม...', i)
        time.sleep(0.5)

t1 = time.time()
###########ขับรถให้เสร็จก่อนแล้วค่อยประชุม###############
# Driving()
# Meeting()

###########Parallel Threading technique###########
# 2. ขับรถไปด้วยประชุมไปด้วย

task1 = threading.Thread(target=Driving)
task2 = threading.Thread(target=Meeting)

print(time.time()) # ดูเวลาเริ่มของ task1
task1.start()
print(time.time()) # ดูเวลาเริ่มของ task2
task2.start()

# เมื่อทำงานเสร็จแล้ว ให้หยุดรอแปปนึง
# ใช้ join เมื่อเราต้องการให้ทำงานพร้อมกัน
task1.join()
task2.join()

t2 = time.time()
print('Time: ', t2 - t1)