#!/usr/bin/env python

import time
import serial

ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

counter = 0

while 1:
    time.sleep(2.4)
    ser.write(str(counter))
    print("Wrote " + str(counter))
    counter += 1
