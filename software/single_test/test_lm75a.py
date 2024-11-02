from machine import I2C
from lm75a import LM75A
from time import sleep_ms

#Init I2C1
i2c = I2C(1)

sensor = LM75A(i2c)

while True:
    print(sensor.temp())
    sleep_ms(100)
    
