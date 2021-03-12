#Transmit from here
import serial
import time
serialcom = serial.Serial('/dev/cu.usbserial-1420', baudrate=9600, timeout=1) #Change port name to the one you are using
from Tx_image import create_data

inn = '11010130101010010'
for i in range(100000):
    inn+='1'
    inn+='0'
inn+='2'
inn = create_data()

print('\nTRANSFERRING DATA:\n')
for i in inn:
    if i == "2":
        serialcom.write("0".encode())
        print("finished")
        break
    serialcom.write((i + '\n').encode())
    time.sleep(0.1)
    print(serialcom.readline().decode('ascii')[:-1])

serialcom.close()