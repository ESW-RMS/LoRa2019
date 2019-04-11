"""
Example for using the RFM9x Radio with Raspberry Pi.

Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Brent Rubell for Adafruit Industries
"""
# Import Python System Libraries
import time
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import RFM9x
import adafruit_rfm9x

# Import more
import threading
import _thread

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None

# Start thread to read input
def input_thread(messages, num_messages):
    while True: 
        text = input()
        messages.append(text)
        num_messages[0] = num_messages[0] + 1

num_messages = [0]
num_printed = 0
messages = []
_thread.start_new_thread(input_thread, (messages, num_messages))

print("RasPi LoRa")
packet = None 
while True:
    # packet = None

    # check for packet rx
    packet = rfm9x.receive()
    if packet is not None:
        # Display the packet text and rssi
        prev_packet = packet
        packet_text = str(prev_packet, "utf-8")
        print("RX: " + packet_text)
        time.sleep(1)

    if num_messages[0] != num_printed:
        # Send new text data
        text_data = bytes(messages[num_printed] + "\r\n", "utf-8")
        rfm9x.send(text_data)
        print("Sent text data: " + messages[num_printed])
        num_printed += 1

    time.sleep(0.1)
