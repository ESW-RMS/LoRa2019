#!/usr/bin/python3

"""
RasPi Zero interface with PCB triphase power reader and LoRa antenna

Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
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
#from numpy import sin
#from math import pi

import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
import subprocess
import serial

# Sending interval in seconds
interval = 600
numSamples = 500
waitTime = .005
currentClampRating = 20

# Create the I2C interface.
# Error here, for whatever reason can't find I2C
#i2c = busio.I2C(board.SCL, board.SDA)

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi2 = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi2, CS, RESET, 915.0)
rfm9x.tx_power = 23

# SPI initialization
spi = spidev.SpiDev()

# Read MCP3008 data
def analogInput(channel):
    spi.max_speed_hz = 1350000
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

# Find frequency from data using fft
# Beta mode
def freq(data):
    #Fs=200.
    #t = [i*1./Fs for i in range(1/waitTime)]
    #fourier = np.fft.fft(data)
    #frequencies = np.fft.fftfreq(len(t), waitTime)
    #positive_frequencies = frequencies[np.where(frequencies >= 0)]
    #magnitudes = abs(fourier[np.where(frequencies >= 0)])  # magnitude spectrum
    #frequency = np.argmax(magnitudes)
    frequency = 60
    return frequency

# Determine voltage value
def volt(data):
    newData = np.absolute(data)
    peakVoltage = np.amax(newData[0,:])
    return peakVoltage

# Returns peak current value (of sine wave form)
def curr(data):
    newData = np.absolute(data)
    x = np.array([np.amax(newData[1,:]), np.amax(newData[2,:]), np.amax(newData[3,:])])
    peakCurrent = np.amax(x)
    return peakCurrent * currentClampRating

light_status = 1

print("RasPi reading from PCB and sending through LoRa")
while True:

    # Read from serial port
    i = 1
    rawData = np.empty([4, numSamples])
    spi.open(0,0)  #open device 1
    for i in range(numSamples):
        for x in range(4):
            rawData[x,i] = analogInput(x) # read from channel x
        time.sleep(waitTime)
    spi.close()
    output = bytes(str(freq(rawData)) + str(volt(rawData)) + str(curr(rawData)) + "\r\n", "utf-8")

    print("Data computed")
    # Write to LoRa
    time.sleep(interval/2) # wait x minutes
    spi.open(0,1) # open device 2
    rfm9x.send(output)
    print("Sent data: " + str(output))
    spi.close() # close device 2
    time.sleep(interval/2) # wait x minutes
