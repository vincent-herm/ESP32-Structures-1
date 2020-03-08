from machine import TouchPad, Pin
from time import sleep

tp1 = TouchPad(Pin(4))
tp2 = TouchPad(Pin(15))

for boucle in range (400) :          # duree de la boucle : 4 s
    etat1 = tp1.read()               # lecture du TouchPad 1
    etat2 = tp2.read()
    print("Touche 1 : {0:3d}  Touche 2 : {1:3d}".format(etat1, etat2))
    sleep(.01)
