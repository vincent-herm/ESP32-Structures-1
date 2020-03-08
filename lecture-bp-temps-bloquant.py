from machine import Pin
from time import sleep

bp = Pin(25, Pin.IN)
compt = 0

for t in range(5):           # on fait juste 5 cycles appui/relachement
    while not bp.value() :   # on attend l'appui sur le bp   
        sleep(.02)           # on attend 20 ms, 50 boucles/s suffisant
    compt = 0   
    while bp.value() :       # on attend l'appui sur le bp   
        compt = compt + 1    # on incremente toutes les 20 ms
        sleep(.02)           # delai entre deux boucles   
    print("Compteur : {0:2d}, soit : {1} s".format(compt, compt /50))