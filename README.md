# Engineering for a Sustainable World: <br> IBEKA 2018-2019

*An overdetailed guide for preparing the IBEKA device from scratch*

Device 1 consists of a custom built PCB that measures triphase current and power from current clamps and a Raspberry Pi. Device 2 consists of a Raspberry Pi and a Particle Electron. Device 1 uses the Raspberry Pi to read in signal information and transfers the data over LoRa communication to Device 2, which uses LoRa communication to read in the data to a Raspberry Pi then sends it over a usb serial connection to a Particle Electron. 

See folders for individual device code. 

# Rasberry Pi Setup

Device components
- RFM9x LoRa Radio 
- RFM9x LoRa Radio antenna
- Raspberry Pi Zero W
- micro SD card with Raspberry Pi OS (Raspian or NOOBS is fine) 
- Raspberry Pi power cable

Device 2 additional components
- micro USB to USB converter
- USB to micro usb cable

During setup
- wiring
- solder setup 
- micro SD card reader 
- micro USB power cord 
- monitor with HDMI input
- HDMI cable
- micro-HDMI to HDMI converter 
- USB keyboard and mouse 
- micro USB to USB converter

## 1. Setup LoRa Wiring

1.1 Solder the antenna to the RFM9x LoRa Radio. 

1.2 Solder the following from the LoRa radio to RasPi 1: 
- (LoRa to RasPi)
- VIN to 3.3 VDC Power
- GND to Ground
- SCK to GPIO 14 SCLK (SPI)
- MISO to GPIO 13 MISO (SPI)
- MOSI to GPIO 12 MOSI (SPI)
- CS to GPIO 11 CE1 (SPI) 
- RST to GPIO 6

Reference for raspberry pi pins: https://pi4j.com/1.2/pins/model-zerow-rev1.html

Reference for troubleshooting wiring: https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/raspberry-pi-wiring

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

At this point the Raspberry Pi bootup screen should be visible on the monitor. 

## 4. Setup ESW Code

Open up a terminal and download the code repository. 

```
cd
git clone https://github.com/ESW-RMS/LoRa2019.git
``` 

To setup the Raspberry Pi for device 1, run the following commands: 

```
cd LoRa2019/device1
./setup_device1.sh
```

For device 2, run this instead: 

```
cd LoRa2019/device2
./setup_device2.sh
```

The setup script can take some time to run to completion. Go get a snack and come back! 

*Note: The setup script appends a line to ~/.profile that runs the startup script on boot or login.*

### If Device 2

Device 2 also needs to disable its serial port. 

1. Run the raspi-config tool. This tool will allow us to easily disable the serial input/output interface that is enabled by default.

```
sudo raspi-config
```

2. This command will load up the Raspberry Pi configuration screen. Use the arrow keys to go down and select “5 Interfacing Options“. Once this option has been selected, you can press Enter.

3. With the next screen you will want to use the arrow keys again to select “P6 Serial“, press Enter once highlighted to select this option.

4. You will now be prompted as to whether you want the login shell to be accessible over serial, select No with your arrow keys and press Enter to proceed.

5. Immediately after you will be asked if you want to make use of the Serial Port Hardware, make sure that you select Yes with your arrow keys and press Enter to proceed.

6. Once the Raspberry Pi has made the changes, you should see the following text appear on your screen.

“The serial login shell is disabled
The serial interface is enabled“.

Instructions copied from https://pimylifeup.com/raspberry-pi-serial/. 

#### If everything is setup correctly, after rebooting the raspberry pi, the onboard LED should blink. Device 1 will blink every 5 seconds. Device 2 will blink once every .1 seconds. 

# Electron setup 

TODO

# Assembly 

Power both Raspberry Pi's. Plug the Electron into the Raspberry Pi for Device 2. 
