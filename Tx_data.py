#Transmit from here
import serial
import time
serialcom = serial.Serial('/dev/cu.usbserial-1410', baudrate=9600, timeout=1) #Change port name to the one you are using


inn = '110101301010100102'
for i in inn:
    if i == "2":
        serialcom.write("0".encode())
        print("finished")
        break
    serialcom.write((i + '\n').encode())
    time.sleep(0.01)
    print(serialcom.readline().decode('ascii')[:-1])

serialcom.close()