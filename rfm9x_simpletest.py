import board
import busio
import digitalio

import adafruit_rfm9x

RADIO_FREQ_MHZ = 915.0

CS = digitalio.DigitalInOut(board.D7)
RESET = digitalio.DigitalInOut(board.D25)

LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

rfm9x.tx_power = 23 

rfm9x.send(bytes("Hello world!\r\n", "utf-8"))
print("Sent Hello World message!")

while True:
    packet = rfm9x.receive()
    if packet is None:
        LED.value = False
        print("Received nothing! Listening again...")

    else: 
        LED.value = True
        print("Received (raw bytes): {0}".format(packet))

        packet_text = str(packet, 'ascii')
        print('Received (ASCII): {0}'.format(packet_text))

        rssi = rfm9x.rssi
        print('Received signal strength: {0} dB'.format(rssi))
