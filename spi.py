# Indonesia RMS 2019
# SPI Interface for MCP3008 and raspi zero
# Tai Kao-Sowa 6/2/19
# Adapted from https://electronicshobbyists.com/raspberry-pi-analog-sensing-mcp3008-raspberry-pi-interfacing/

# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay
import RPi.GPIO as GPIO	# To use GPIO pins

# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Convert the data to useful info
def convert(data):
  newData = (data * 1) / float(1)
  newData = round(newData, 2) # Round off to 2 decimal places
  return newData

while True:
	output = analogInput(0) # Reading from CH0
	output = convert(output) # Convert the data to useful stuff

	print(output)
    # Do other stuff here to upload data to cloud
  	sleep(5)
