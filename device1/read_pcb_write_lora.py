#!/usr/bin/python3

"""
Example for using the RFM9x Radio with Raspberry Pi.

Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Brent Rubell for Adafruit Industries
"""
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
import threading
import _thread
import subprocess
import spidev # To communicate with SPI devices
import numpy as np

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23

# Start SPI connection
spi2 = spidev.SpiDev()
spi2.open(0,0)

# Read MCP3008 data
def analogInput(channel):
  spi2.max_speed_hz = 1350000
  adc = spi2.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Convert the data to useful info
def convert(data):
  a = np.array(data)
  newData = np.absolute(a)
  peak = np.amax(a)
  newData = round(newData, 2) # Round off to 2 decimal places
  # return array [Peak voltage, frequency]
  return newData

light_status = 1

print("RasPi reading from PCB and sending through LoRa")
while True:

    ## Read from serial port
    #i = 1
    #rawData = np.empty([4, 100])
    
    #while i < 100:
    #  print(i)
    #  for x in range(4):
    #    rawData[x,i] = analogInput(x) # read from channel x
    #  time.sleep(.01)
    
    #output = convert(output) # Convert the data to useful stuff
    
    output = "Hello world\n"

    # Send data to LoRa
    text_data = bytes(str(output) + "\r\n", "utf-8")
    rfm9x.send(text_data)
    print("Sent data: " + str(output))

    # Toggle RasPi onboard light
    subprocess.run(["echo " + str(light_status) + " >/sys/class/leds/led0/brightness"], shell=True)
    light_status = 1 - light_status

    time.sleep(5)
