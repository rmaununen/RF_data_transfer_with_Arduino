#Receive here
import serial
import time
#1410 or 1420
serialcom = serial.Serial('/dev/cu.usbserial-1420', baudrate=9600, timeout=1) #Change port name to the one you are using

receiving = True
time.sleep(2)
received_data = []
serialcom.write("1\n".encode())
time_init = time.time()
print('start time: ', time_init)
while receiving:
    bytesToRead = serialcom.inWaiting()
    data = serialcom.read(bytesToRead).decode('ascii')[:-2]
    if not data == '':
        received_data.append(data)
    time.sleep(0.01) #must be faster than the arduino
    time_cur = time.time()
    if (time_cur - time_init) >= 5:
        receiving = False
        serialcom.write("0\n".encode())
        time.sleep(0.4)
        print('end time: ', time_cur)

bytesToRead = serialcom.inWaiting()
data = serialcom.read(bytesToRead).decode('ascii')[:-2]
serialcom.close()
print(data)
'''
received_data.append(data[0])
received_data.append(data[1])
print(data[2])
print(data[3])
'''

print('\n', received_data)
print('length of the received array: ', len(received_data))