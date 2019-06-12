# Engineering for a Sustainable World - IBEKA Project 2018-2019

*An overdetailed guide for preparing the IBEKA device from scratch*

Device 1 consists of RasPi 1. Device 2 consists of RasPi 2 and Electron. RasPi 1 reads in signal information and transfers the data over LoRa communication to RasPi 2, which uses LoRa communication to read in the data and sends it over a usb serial connection to a Particle Electron. 

See folders for individual device code. 

# RasPi 1 Setup

Components: 
- RFM9x LoRa Radio 
- RFM9x LoRa Radio antenna
- RasPi 1
- micro SD card with RasPi OS (Raspian or NOOBS is fine) 
- USB3 to power 
- Any kind of preferred wire 

For RasPi setup
- micro SD card reader 
- hdmi cable
- micro usb power cord 
- HDMI to micro-HDMI converter 
- monitor with HDMI input
- USB keyboard and mouse 
- USB to micro USB

## Setup RasPi basics 

If you have an operating system preinstalled on the micro SD card, then skip section 1 ("Prepare the micro SD card"). 

### 1. Prepare the micro SD card 

1. Download balenaEtcher at https://www.balena.io/etcher/. 

2. Download the NOOBS zip file at https://www.raspberrypi.org/downloads/noobs/. 

3. Open balenaEtcher and follow the instructions to flash NOOBS onto the micro SD card. 

### 2. Plug everything in

1. Plug in the micro SD card. 

2. Plug the HDMI cable into the HDMI cable to micro-HDMI converter, then into RasPi 1. Plug the other end of the HDMI cable into the monitor. 

3. Plug the keyboard and mouse into RasPi 1 using the USB to micro USB converter. 

4. Plug in the power cord. 

## Setup LoRa Wiring

Solder the antenna to the RFM9x LoRa Radio. 

Connect the following wires: 
- VIN to TODO
- GND to TODO
- SCK to TODO
- TODO

## Setup LoRa Software

## Setup ESW Program

# RasPi 2 setup

TODO 

# Electron setup 

TODO
