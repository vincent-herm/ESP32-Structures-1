from time import sleep
from machine import Pin, SPI, I2C
from sx1276 import SX127x
from ssd1306_i2c import Display

device_config = {
    'miso':19,
    'mosi':27,
    'ss':18,
    'sck':5,
    'dio_0':26,
    'reset':14,
    'led':2, 
}


device_spi = SPI(baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_config['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_config['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_config['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_config)
display = Display()

def receive(lora):
    print("LoRa Receiver")
    display = Display()
    display.show_text("En attente...",False)
    while True:
        if lora.received_packet():
            lora.blink_led(times = 1, on_seconds = 0.01, off_seconds = 0.01)
            print('something here')
            payload = lora.read_payload()
            display.show_text("reception...",False)
            display.show_text("{0}".format(payload),0,14,False)
            display.show_text("RSSI: {}".format(lora.packet_rssi()),0,30,False)
            print(payload)

#if __name__ == '__main__':
receive(lora)

