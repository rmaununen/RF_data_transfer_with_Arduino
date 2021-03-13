#Transmit from here
import serial
import time
#1410 or 1420
serialcom = serial.Serial('/dev/cu.usbserial-1420', baudrate=9600, timeout=1) #Change port name to the one you are using
from Tx_image import create_data
from Tx_text import create_text

transfer = 'image'
if transfer == 'text':
    inn = create_text()

elif transfer == 'image':
    inn = create_data() 
'''
inn = ''
for i in range(100000):
    inn += '1'
inn+='2'
'''
print('\nTRANSFERRING DATA:\n')
for i in inn:
    if i == "2":
        serialcom.write("0".encode())
        print("finished")
        break
    serialcom.write((i + '\n').encode())
    time.sleep(0.001)
    print(serialcom.readline().decode('ascii')[:-1])

serialcom.close()