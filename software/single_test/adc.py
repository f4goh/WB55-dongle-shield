"""
analog read ADC 12 bits (mots de 16 bits)
"""

from machine import ADC
from pyb import Pin
from time import sleep_ms
import sys

led_out = Pin('A9', Pin.OUT_PP, Pin.PULL_NONE) # Broche de la LED
adc = ADC('A0')

while True:
    try:
        valeur=adc.read_u16()//64
        sleep_ms(100)
        print(valeur)
        if valeur>500:
            led_out.value(1)
        else:
            led_out.value(0)
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        sys.exit()