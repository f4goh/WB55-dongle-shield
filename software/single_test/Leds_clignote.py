from pyb import LED
from time import sleep_ms

led1 = LED(1)
led2 = LED(2)
led3 = LED(3)


while True:
    led1.on()
    sleep_ms(1000)
    led1.off()
    led2.on()
    sleep_ms(1000)
    led2.off()
    led3.on()
    sleep_ms(1000)
    led3.off()



