# calculate_time.py
from datetime import datetime

# คำนวณค่าที่จอดรถโดยโชว์จำนวนวัน และจำนวนชั่วโมง รวมราคาค่าที่จอดรถด้วย

def calculate_car_t_hour(dt='2022-05-08 12:27:18',first_hour=20,next_hour=10):
	# only hour and minute
	convert = datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
	now = datetime.now()
	delta = now - convert
	day = delta.days
	hour = delta.seconds // 3600
	minute = (delta.seconds % 3600) // 60
	print('Parking time: {} days {} Hours {} minutes'.format(day,hour,minute))
	total = []
	if day > 0:
		total.append(first_hour * day * 24)
		total.append((hour -1) * next_hour)
	elif hour > 1:
		# ชั่วโมงแรก
		total.append(first_hour) # ชั่วโมงแรก 20
		total.append((hour - 1) * next_hour) # ชั่วโมงถัดไป
	elif hour == 1:
		total.append(first_hour)

	if minute > 15 and hour >= 1:
		total.append(next_hour)
	elif minute > 15 and hour == 0:
		total.append(first_hour)
	elif minute < 15:
		pass

	cal = sum(total)
	print('Car park fee: {} baht'.format(cal))

calculate_car_t_hour('2022-05-08 8:27:18')

################################################################################
###------คำนวณจำนวณชั่วโมงที่จอดรถ------

def calculate_car_hour(dt='2022-05-08 12:27:18',first_hour=20,next_hour=10):
	# only hour and minute
	convert = datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
	now = datetime.now()
	delta = now - convert
	hour = delta.seconds // 3600
	minute = (delta.seconds % 3600) // 60
	print('Parking time: {} Hours {} minutes'.format(hour,minute))
	total = []
	if hour > 1:
		# ชั่วโมงแรก
		total.append(first_hour) # ชั่วโมงแรก 20
		total.append((hour - 1) * next_hour) # ชั่วโมงถัดไป
	elif hour == 1:
		total.append(first_hour)

	if minute > 15 and hour >= 1:
		total.append(next_hour)
	elif minute > 15 and hour == 0:
		total.append(first_hour)
	elif minute < 15:
		pass

	cal = sum(total)
	print('Car park fee: {} baht'.format(cal))

calculate_car_hour('2022-05-08 8:27:18')

################################################################################
###------วิธีการคิดคำนวณ------
from datetime import timedelta

# เก็บค่าวันที่ไว้ที่ตัวแปร
dt = '2022-02-15 12:36:39'

# เปลี่ยนในเป็นฟอร์แมตของวันที่
convert = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
convert
#datetime.datetime(2022, 2, 15, 12, 36, 39)

# เวลาปัจจุบัน
now = datetime.now()
now
#datetime.datetime(2022, 6, 5, 15, 40, 40, 811681)

# ถ้าใช้ delta จะแสดงจำนวน วัน วินาที และ ไมโครวินาที
delta = now - convert
delta
#datetime.timedelta(days=110, seconds=11041, microseconds=811681)

# หาจำนวนชั่วโมง ถ้าใช้ / จะมีเศษของชั่วโมง (ไม่ใช่เศษนาที)
delta.seconds / 3600 # find how many hours
#3.0669444444444443

# ใช้ // จะได้ชั่วโมงที่เป็นจำนวนเต็ม
hour = delta.seconds // 3600
hour
#3

# หาจำนวนนาที โดยใช้ % คำนวณเศษของชั่วโมงก่อน แล้วค่อยตามด้วย // คำนวนจำนวนนาที
minute = (delta.seconds % 3600) // 60
minute
