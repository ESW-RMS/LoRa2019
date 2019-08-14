#!/usr/bin/python3

"""
Device code for no Radio

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

# Sending interval in seconds
#interval = 600
interval = 1 #for testing
numSamples = 500
waitTime = .005
currentClampRating = 20

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Read MCP3008 data
#def analogInput(channel):
#    adc = spi.xfer2([1,(8+channel)<<4,0])
#    data = ((adc[1]&3) << 8) + adc[2]
#    return data

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
#def volt(data):
#    newData = np.absolute(data)
#    peakVoltage = np.amax(newData[0,:])
#    return peakVoltage

# Returns peak current value (of sine wave form)
#def curr(data):
#    newData = np.absolute(data)
#    x = np.array([np.amax(newData[1,:]), np.amax(newData[2,:]), np.amax(newData[3,:])])
#    peakCurrent = np.amax(x)
#    return peakCurrent * currentClampRating

print("RasPi reading from PCB and sending through LoRa")
while True:

    # Commented out for testing
    # Read from serial port
    #i = 1
    #rawData = np.empty([4, numSamples])
    #spi.open(0,0)  #open device 1
    #for i in range(numSamples):
    #    for x in range(4):
    #        rawData[x,i] = analogInput(x) # read from channel x
    #    time.sleep(waitTime)
    #output = bytes(str(freq(rawData)) + str(volt(rawData)) + str(curr(rawData)) + "\r\n", "utf-8")

    output = "hello world\r\n"
    # Send to serial
    packet_text = str(output, "utf-8") #bytes(prev_packet, "utf-8")
    print("Sent to serial: " + packet_text)
    ser.write(packet_text.encode('utf-8').strip())
    time.sleep(interval)
