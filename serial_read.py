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

while 1:
    x=ser.readline()
    if len(x) != 0:
        print(x)
        print("Read something!")
        ser.write("A")
