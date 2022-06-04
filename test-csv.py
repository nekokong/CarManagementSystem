# test-csv.py

import csv

# 'a' = append new value
def writetocsv(data):
    # data = ['toyota', 'red', '1A11', '1011', '2022-05-07 15:29:15']
    with open('test_savecsv.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data) # no 's' is single line append = row not rows
    print('csv saved')
    
data = ['toyota', 'red', '1A11', '1011', '2022-05-07 15:29:15']
#writetocsv(['A','B'])
print(data)
writetocsv(data)

# Split text from '|'
#text = 'toyota|red|1A11|1011|2022-05-07 15:29:15'
#text.split('|')
#['toyota', 'red', '1A11', '1011', '2022-05-07 15:29:15']

##########################################3
# Create unique key by uuid
import uuid

# uuid code will split digit by '-'
uuid.uuid1()

# uuid hex will not split
uuid.uuid1().hex

# for loop generate key
for i in range(10):
    print(uuid.uuid1())

# for loop generate key by hex
for i in range(10):
    print(uuid.uuid1().hex)

# for loop generate key
# change uuid to string
# split text by '-'
for i in range(10):
    print(str(uuid.uuid1()).split('-'))

# for loop generate key
# change uuid to string
# split text by '-'
# key 8 digits from index 0
for i in range(10):
    print(str(uuid.uuid1()).split('-')[0])

################################    

# check text size
import sys

sys.getsizeof(t)
t = 'in|toyota|red|1A11|1011|2022-05-07 15:29:15'

# size of 1 character
sys.getsizeof(t+'a') - sys.getsizeof(t)