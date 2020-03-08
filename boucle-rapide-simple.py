from machine import Pin
from time import sleep, sleep_ms

led_bleue = Pin(2, Pin.OUT)
led_verte = Pin(23, Pin.OUT)
compt = 0

while compt < 400  :             # on arrete la While apres 4 secondes
    compt +=1                    # on incremente chaque 10 ms
    if compt % 50 == 0 :         # compt % 50 est vrai chaque 0.5 s 
        led_bleue.value(not led_bleue.value()) # on bascule la LED bleue.
    if (compt + 25) % 50 == 0 :  # vrai chaque 0.5 s, mais 0.25 s plus tot
        led_verte.value(not led_verte.value()) # on bascule la LED verte  
    sleep_ms(10)                 # temps de cycle 10 ms


