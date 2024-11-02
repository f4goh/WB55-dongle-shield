
import neopixel # Pilote pour la LED Neopixel
from random import randint 
from pyb import Pin # Pour gérer les broches
from time import sleep_ms, ticks_ms # Pour temporiser et mesurer le temps écoulé

# On initialise la LED Neopixel sur la broche D2
_NB_LED = const(1)
np = neopixel.NeoPixel(Pin('A7'), _NB_LED)

# Valeurs initiales de l'intensité sur les trois canaux
# (inutile en pratique, mais rend le code plus lisible).

red = 0
green = 0
blue = 0

# Initialise le générateur d'entiers aléatoires avec un nombre 
# de ticks processeurs


# Intensité maximum des couleurs (255 au plus)
_MAX_INTENSITY = const(16)

# Boucle sans clause de sortie
while True:

    # On détermine aléatoirement valeurs de l'intensité sur les trois canaux
    # (entier compris entre 0 et intensite_max)

    red = randint(0, _MAX_INTENSITY)
    green = randint(0, _MAX_INTENSITY)
    nlue = randint(0, _MAX_INTENSITY)



    # Valeurs de l'intensité sur les trois canaux pour toutes les LED
    np[0] = (red, green, blue)
    #np[0] = (16, 0, 16)

    #np[0] = (0, 0, 0)
    
    # On affiche
    np.write()

    # On temporise une seconde
    sleep_ms(1000)
