import csv
import serial
import time
from itertools import islice




with open('test1.csv','rt', encoding='UTF-8') as f:
    cr = csv.reader(f)
    cmd_line = list(filter(None,list(cr)))
    print(cmd_line)
    PORTNAME =  cmd_line[0][0]
    BAUDRATE =  int(cmd_line[0][1])
    DATABIT = int(cmd_line[0][2])
    PARITY = cmd_line[0][3]
    STOPBIT = int(cmd_line[0][4])

ser = serial.Serial(PORTNAME,BAUDRATE,DATABIT,PARITY,STOPBIT)

for line in islice(cmd_line,1,None):
    line = line[1].replace("0x","")
    print(line)
    ser.write(bytes.fromhex(line))
    time.sleep(0.5)

ser.close()