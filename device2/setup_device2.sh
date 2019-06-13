#!/bin/bash 

sudo apt-get update
sudo apt-get upgrade

# Download LoRa Libraries 
# Reference: https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/rfm9x-raspberry-pi-setup
#sudo pip3 install adafruit-circuitpython-ssd1306
#sudo pip3 install adafruit-circuitpython-framebuf
sudo pip3 install adafruit-circuitpython-rfm9x

# Set to run on startup 
echo "/home/pi/LoRa2019/device2/start_device2.sh" >> ~/.profile
