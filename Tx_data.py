#Transmit from here
import serial
import time
serialcom = serial.Serial('/dev/cu.usbserial-1410', 9600, 1) #Change port name to the one you are using

While True:
    i = int(input('input (1 or 0): ').strip())
    if i == 2:
        print("finished")
        break
    serialcom.write(i.encode())
    print(serialcom.readline().decode('ascii'))
serialcom.close()