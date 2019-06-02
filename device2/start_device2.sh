#! /bin/sh
### BEGIN INIT INFO
# Provides:          start_device2
# Required-Start:    $all
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:
# Short-Description: Starts the device 2 script
### END INIT INFO

# /etc/init.d/start_device2

sudo chmod 777 /sys/class/leds/led0/trigger
sudo chmod 777 /sys/class/leds/led0/brightness

echo none >/sys/class/leds/led0/trigger

/home/pi/LoRa2019/device2/read_lora_write_serial.py
