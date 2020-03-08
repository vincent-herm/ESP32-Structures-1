from machine import Pin
from time import sleep

bp = Pin(25, Pin.IN)
compt = 0
ancien_etat = bp.value()            # initialisation ancien_etat

for t in range(500):                # on fait 500 cycles * 0.02 s = 10 s
    etat = bp.value()               # lecture etat
    if etat :                       # tant qu'on appuie...
        compt = compt + 1           # ... on incremente 
    if ancien_etat and not etat :   # et si front descendant ! ...
        print("Compteur : {0:2d}, soit : {1} s".format(compt, compt /50))
        compt = 0                   # on affiche et remet a 0
    ancien_etat = etat              # memorisation etat boucle avant
    sleep(0.02)                     # delai de boucle
