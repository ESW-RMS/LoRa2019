#!/usr/bin/env python3

import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    ser.write(b'A')
    print("Wrote to serial port")
    time.sleep(2)

