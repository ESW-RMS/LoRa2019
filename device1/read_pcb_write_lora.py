#!/usr/bin/python3

"""
Example for using the RFM9x Radio with Raspberry Pi.
Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Brent Rubell for Adafruit Industries

Old code: doesn't have EE stuff implemented
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
# I made up this stuff. Real calculations to come
def convert(data):
  newData = (data * 1) / float(1)
  newData = round(newData, 2) # Round off to 2 decimal places
  return newData

light_status = 1

print("RasPi reading from PCB and sending through LoRa")
while True:

    ## Read from serial port
    #output = analogInput(0) # Reading from CH0
    #output = convert(output) # Convert the data to useful stuff
    ## Repeat the above code for CH1, CH2, CH3
    output = "Hello world\n"

    # Send data to LoRa
    text_data = bytes(str(output) + "\r\n", "utf-8")
    rfm9x.send(text_data)
    print("Sent data: " + str(output))

    # Toggle RasPi onboard light
    subprocess.run(["echo " + str(light_status) + " >/sys/class/leds/led0/brightness"], shell=True)
    light_status = 1 - light_status

    time.sleep(5)
