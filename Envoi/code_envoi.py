
#import LoRaDuplexCallback
#import LoRaPingPong
#import LoRaSender

from time import sleep, ticks_ms
from machine import Pin, SPI, I2C
from sx1276 import SX127x
from ssd1306_i2c import Display

from machine import Pin, I2C, TouchPad
from time import sleep, sleep_us, sleep_ms, ticks_ms, ticks_us

device_config = {
    'miso':19,
    'mosi':27,
    'ss':18,
    'sck':5,
    'dio_0':26,
    'reset':14,
    'led':2, 
}
compt = 0

device_spi = SPI(baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_config['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_config['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_config['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_config)
display = Display()

def synchro_us(temps_cycle) :
    global compt, top, somme
    if compt == 0 :
        top = ticks_us() ; somme = 0
    tip = ticks_us()
    delta = tip - top
    compt = compt + 1
    attente = temps_cycle * compt - delta
    somme = somme + attente
    #print("delta : {0:5d}; compt : {1:2d}; attente : {2:6d}; somme : {3:7d} ".format(delta, compt, attente, somme, top, tip, attente))
    print(delta)
    sleep_us((attente))
    
    
def send(lora):
    counter = 0
    print("LoRa Sender")
    start = ticks_ms()
    while True:
        stop = ticks_ms()
        #payload = 'Hello ({0}) temps = {1}'.format(counter, stop-start)
        payload = '{0} temps : {1}'.format(counter, stop-start)
        print("Sending packet: \n{}\n".format(payload))
        display.show_text("envoi...",False)
        display.show_text("{0}".format(payload),0,15,False)
        display.show_text("RSSI: {}".format(lora.packet_rssi()),0,30,False)
        #display.show_text_wrap("{0} RSSI: {1}".format(payload, lora.packet_rssi()),2,10,clear_first = False)
        lora.println(payload)
        counter += 1
        synchro_us(100000)           
            

#if __name__ == '__main__':
send(lora)

