# Engineering for a Sustainable World: <br> IBEKA 2018-2019

*An overdetailed guide for preparing the IBEKA device from scratch*

Device 1 consists of a custom built PCB that measures triphase current and power from current clamps and a Raspberry Pi. Device 2 consists of a Raspberry Pi and a Particle Electron. Device 1 uses the Raspberry Pi to read in signal information and transfers the data over LoRa communication to Device 2, which uses LoRa communication to read in the data to a Raspberry Pi then sends it over a usb serial connection to a Particle Electron. 

See folders for individual device code. 
Detailed assembly guide: https://docs.google.com/document/d/1eoOL6ycpx3u1b9OP86EHPXVrBaiWyDBE23J0aYlFA0I/edit?usp=sharing

# Raspberry Pi Setup

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
Just raspbian: https://thepi.io/how-to-install-raspbian-on-the-raspberry-pi/
With NOOBS: https://thepi.io/how-to-install-noobs-on-the-raspberry-pi/

2.1 Download balenaEtcher at https://www.balena.io/etcher/. 

2.2 Download the NOOBS zip file at https://www.raspberrypi.org/downloads/noobs/. 

2.3 Open balenaEtcher and follow the instructions to flash NOOBS onto the micro SD card. 

## 3. Plug everything in

3.1 Plug in the micro SD card. 

3.2 Plug the HDMI cable into the HDMI cable to micro-HDMI converter, then into RasPi 1. Plug the other end of the HDMI cable into the monitor. 

3.3 Plug the keyboard and mouse into RasPi 1 using the USB to micro USB converter. 

3.4 Plug in the power cord. 

At this point the Raspberry Pi bootup screen should be visible on the monitor.

Fyi, Pi password is "raspberry" or "rms" or "esw"

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
If the terminal shows bash: ./setup_device1.sh: Permission denied then run the following commands:

```
sudo chmod +x setup_device1.sh
./setup_device1.sh
```
Do the same thing for device 2 if permission is denied.
For device 2, run this instead: 

```
cd LoRa2019/device2
./setup_device2.sh
```

The setup script can take some time to run to completion. Go get a snack and come back! 

*Note: The setup script appends a line to ~/.profile that runs the startup script on boot or login.*
Device 2 also needs to disable its serial port.

Run the raspi-config tool to enable SPI.
sudo raspi-config
This command will load up the Raspberry Pi configuration screen. Use the arrow keys to go down and select “5 Interfacing Options“. Then enable SPI. You might also want to enable SSH: when the electron is plugged into the RasPi there's no port for the keyboard, so SSHing in over wifi is the only way to access it.

### If Device 2

Device 2 also needs to disable its serial port. 

1. Run the raspi-config tool.

```
sudo raspi-config
```

2. Use the arrow keys to go down and select “5 Interfacing Options“. Once this option has been selected, you can press Enter.

3. With the next screen you will want to use the arrow keys again to select “P6 Serial“, press Enter once highlighted to select this option.

4. You will now be prompted as to whether you want the login shell to be accessible over serial, select No with your arrow keys and press Enter to proceed.

5. Immediately after you will be asked if you want to make use of the Serial Port Hardware, make sure that you select Yes with your arrow keys and press Enter to proceed.

6. Once the Raspberry Pi has made the changes, you should see the following text appear on your screen.

“The serial login shell is disabled
The serial interface is enabled“.

Instructions copied from https://pimylifeup.com/raspberry-pi-serial/. 

#### If everything is setup correctly, after rebooting the raspberry pi, the onboard LED should blink. Device 1 will blink every 5 seconds. Device 2 will blink once every .1 seconds. 

If the raspi gives you a black screen when connected to the monitor (and the monitor is on) edit /boot/config.txt by plugging the microSD card into your computer and uncomment hdmi_safe=1
From config.txt:
```
# uncomment if you get no picture on HDMI for a default "safe" mode
hdmi_safe=1
```

# Electron setup 

There’s one Particle Electron per location. Follow the tutorial here to set it up: https://community.particle.io/t/electron-3rd-party-sim-tips/26490. For most efficient/painless process, would recommend reading this page first to understand how to setup a 3rd-party SIM card, then gathering the relevant required info (ICCID and APN), and then completing the tutorial itself. 

Helpful page to decipher blinking LEDs: https://docs.particle.io/tutorials/device-os/led/electron/.

Complete the following process for each Electron:
Ask Dygdha to determine the location’s appropriate cell service provider and network. For the 2 Sumba locations = Telkomsel 2G, the 2 Mt. Ciptagelar locations = XL 3G
Upon arrival in Indonesia, purchase and activate the appropriate SIM card based on provider and network
We activated SIM card by putting in your phone. Call someone and receive a call...should be activated

While SIM card still in phone, determine the ICCID of the SIM card. Follow Android (https://www.wikihow.tech/Find-Your-Sim-Card-Number-on-Android) or iPhone (https://twigby.zendesk.com/hc/en-us/articles/213023857-How-can-I-find-my-SIM-card-number-ICCID-on-my-iPhone) tutorial. For example, determined ICCID of Telkomsel 2G SIM card was 8962100085329251238 (but each SIM card will have its own ICCID)

To determine the APN for the location, ask Dygdha or Google “[provider] APN 2019 [network]”
For example, Google “Telkomsel APN 2019 3G”. Determine the APN is “telkomsel.” Dygdha mentioned that 2G and 3G should be same APN for respective providers. May change year to year, look up for current year. Although each SIM card will have unique ICCID, APN will be same for SIM cards with same provider and network types. XL was “Internet”

Now that you’ve gathered the necessary info, time to follow the Particle Electron tutorial for 3rd-party SIM card: https://community.particle.io/t/electron-3rd-party-sim-tips/26490 

At Step 2 of setup.particle.io, after downloading the custom firmware file, move it into your computer’s main directory. For ex on Mac: put firmware file in /Users/Zach directory
Instead of following the tutorial’s Step 3, do the next steps. Download Node.js. This page helps with downloading the Particle CLI: https://docs.particle.io/tutorials/developer-tools/cli/ 
Open Finder (for Mac) and follow the filepath to “Mac/Users/Zach/bin” The bin file is when running the CLI download Terminal command 
Double-click the “particle” file
Run the command in Terminal: particle login
Follow Terminal’s instructions to login (using the Particle Electron Cloud Login Information provided above)
If this doesn’t work for later steps, try the provided Step 2 instructions
e.  You’re finished with this subprocedure. Continue with Step 4. 
f.  You will be prompted to name the Electron. Before doing so, visit the IFTTT portal (https://ifttt.com/my_applets) and notice how the previous Electrons have been named (ex: 1819sumba1 corresponds to the Sumba Kamanjara installation). The name you assign to this Electron must match when you create its corresponding Applet in IFTTT aka it’s the link between the two systems 

Once you’ve successfully completed the entire tutorial, you will be taken to the website “build.particle.io” From here, you can write your own Particle App or load an existing updated one created during your ESW year (by making sure the Electron is connected to your computer via USB and then clicking the Flash (lightning bolt) icon. The 18-19 code is ESW_IBEKA_1819_MAIN
When flashing the code to the desired Electron, look in the bottom right corner of the black code screen and make sure the device name is the desired Electron device. If so, flash. If not, click Devices in the left toolbar and click the desired device to star it. Returning to the code window, it should now be in the bottom right corner, allowing you to flash the code to it. In order to flash a program to the Electron, the Electron must be connected with USB to your computer, no flashing over wifi.

Make sure in the command “Particle.publish("SUM2_DATA", c, PUBLIC),” the first argument matches in IFTTT the Event Name first step.


# Assembly 
See the guide: https://docs.google.com/document/d/1eoOL6ycpx3u1b9OP86EHPXVrBaiWyDBE23J0aYlFA0I/edit?usp=sharing
