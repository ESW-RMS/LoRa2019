#!/usr/bin/python3

"""
Example for using the RFM9x Radio with Raspberry Pi.

Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Brent Rubell for Adafruit Industries
"""
# Import Python System Libraries
import time
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import RFM9x
import adafruit_rfm9x

# Import more
import threading
import _thread
import subprocess

# Create SPI interface
import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Convert the data to useful info
# I made up this stuff. Real calculations to come
def convert(data):
  newData = (data * 1) / float(1)
  newData = round(newData, 2) # Round off to 2 decimal places
  return newData

# Start thread to read input
def input_thread(messages, num_messages):

    # Start SPI connection
    spi = spidev.SpiDev() # Created an object
    spi.open(0,0)

    while True:
        output = analogInput(0) # Reading from CH0
        output = convert(output) # Convert the data to useful stuff
        # Repeat the above code for CH1, CH2, CH3

        messages.append(output)
        num_messages[0] += 1
        sleep(5)

num_messages = [0]
num_printed = 0
messages = []
_thread.start_new_thread(input_thread, (messages, num_messages))

light_status = 1

print("RasPi reading from PCB and sending through LoRa")
packet = None
while True:

    if num_messages[0] != num_printed:
        # Send new text data
        text_data = bytes(messages[num_printed] + "\r\n", "utf-8")
        rfm9x.send(text_data)
        print("Sent text data: " + messages[num_printed])
        num_printed += 1

        # Toggle RasPi onboard light
        subprocess.run(["echo " + str(light_status) + " >/sys/class/leds/led0/brightness"], shell=True)
        light_status = 1 - light_status

    time.sleep(0.5)
