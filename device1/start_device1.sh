#! /bin/sh
### BEGIN INIT INFO
# Provides:          start_lora
# Required-Start:    $all
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:
# Short-Description: Starts the LoRa python script
### END INIT INFO

# /etc/init.d/start_device1

sudo chmod 777 /sys/class/leds/led0/trigger
sudo chmod 777 /sys/class/leds/led0/brightness

echo none >/sys/class/leds/led0/trigger

/home/pi/LoRa2019/device1/read_pcb_write_lora.py
