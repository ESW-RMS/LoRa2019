# Engineering for a Sustainable World: <br> IBEKA 2018-2019

*An overdetailed guide for preparing the IBEKA device from scratch*

Device 1 consists of RasPi 1. Device 2 consists of RasPi 2 and Electron. RasPi 1 reads in signal information and transfers the data over LoRa communication to RasPi 2, which uses LoRa communication to read in the data and sends it over a usb serial connection to a Particle Electron. 

See folders for individual device code. 

# Rasberry Pi Setup

Device components
- RFM9x LoRa Radio 
- RFM9x LoRa Radio antenna
- RasPi 1
- micro SD card with RasPi OS (Raspian or NOOBS is fine) 
- RasPi power cable

For setup
- Wiring
- Solder
- micro SD card reader 
- hdmi cable
- micro usb power cord 
- HDMI to micro-HDMI converter 
- monitor with HDMI input
- USB keyboard and mouse 
- USB to micro USB

## 1. Setup LoRa Wiring

1.1 Solder the antenna to the RFM9x LoRa Radio. 

1.2 Connect the following with wires from the LoRa radio to RasPi 1: 
- (LoRa to RasPi)
- VIN to 3.3 VDC Power
- GND to Ground
- SCK to GPIO 14 SCLK (SPI)
- MISO to GPIO 13 MISO (SPI)
- MOSI to GPIO 12 MOSI (SPI)
- CS to GPIO 11 CE1 (SPI) SPI Chip Select
- RST to GPIO 6

Reference for raspberry pi pins: https://pi4j.com/1.2/pins/model-zerow-rev1.html
Photos of the setup are included in the folder 'setup_photos'. 

#### If you have an operating system preinstalled on the micro SD card, then skip section 2 ("Prepare the micro SD card"). 

## 2. Prepare the micro SD card 

2.1 Download balenaEtcher at https://www.balena.io/etcher/. 

2.2 Download the NOOBS zip file at https://www.raspberrypi.org/downloads/noobs/. 

2.3 Open balenaEtcher and follow the instructions to flash NOOBS onto the micro SD card. 

## 3. Plug everything in

3.1 Plug in the micro SD card. 

3.2 Plug the HDMI cable into the HDMI cable to micro-HDMI converter, then into RasPi 1. Plug the other end of the HDMI cable into the monitor. 

3.3 Plug the keyboard and mouse into RasPi 1 using the USB to micro USB converter. 

3.4 Plug in the power cord. 

At this point the raspberry pi bootup screen should be visible on the monitor. 

## 4. Setup ESW Code

Open up a terminal and download the code repository. 

```
cd
git clone https://github.com/ESW-RMS/LoRa2019.git
``` 

To setup the raspberry pi for device 1, run the following commands: 

```
cd LoRa2019/device1
./setup_device1.sh
```

For device 2, run this instead: 

```
cd LoRa2019/device2
./setup_device2.sh
```

The setup script can take around X minutes to run to completion. Go get a snack and come back! 

*Note: The setup script appends a line to ~/.profile that runs the startup script on boot or login.*

If everything is setup correctly, after rebooting the raspberry pi, the onboard LED should blink. RasPi 1 will blink every 5 seconds. RasPi 2 will blink once every .1 seconds. 

# Electron setup 

TODO

# Assembly 

Power both raspberry pis. Plug the electron into the raspberry pi for device 2. 
