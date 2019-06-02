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
import subprocess
import serial

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None

# Configure Serial Port 
ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

# Light to track status
light_status = 1

print("RasPi reading from LoRa and writing to serial")
packet = None 
while True:

    # check for packet rx
    packet = rfm9x.receive()
    if packet is not None:
        # Display the packet text and rssi
        prev_packet = packet
        packet_text = prev_packet.encode('utf-8').strip()

        # Send the packet text to serial 
        ser.write(packet_text)
        print("RX: " + packet_text)

        # Toggle light
        subprocess.run(["echo " + str(light_status) + " >/sys/class/leds/led0/brightness"], shell=True)
        light_status = 1 - light_status
        
        time.sleep(1)

    time.sleep(0.1)
