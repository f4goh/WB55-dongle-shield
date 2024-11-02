#Test all

from machine import I2C
from ssd1306 import SSD1306_I2C
from time import sleep,sleep_ms
from pyb import Pin # Pour gérer les GPIO
from neopixel import NeoPixel # Pilote pour la LED Neopixel
from lm75a import LM75A
from onewire import OneWire
from ds18x20 import DS18X20
from machine import ADC
import sys



#Init I2C1
i2c = I2C(1)

bp = Pin('A8', Pin.IN, Pin.PULL_UP)
led = Pin('A9', Pin.OUT_PP, Pin.PULL_NONE) # Broche de la LED
np = NeoPixel(Pin('A7'), 1)
sensorLm75 = LM75A(i2c)
bus = OneWire(Pin('A1'))
ds = DS18X20(bus)
sensorDs = ds.scan()
adc = ADC('A0')
oled = SSD1306_I2C(128, 64, i2c)


led.value(0)

state=0


def interruption_handler(pin):
    global state
    state=(state+1)%6

bp.irq(trigger=Pin.IRQ_FALLING,handler=interruption_handler)
    

def i2cScan():
    lst=i2c.scan()
    print(lst)
    oled.fill(0)
    oled.text("Scan I2C", 0, 0)
    for n in range(len(lst)):
        oled.text(str(hex(lst[n])), 0, 10*(n+1))
    oled.show()
    sleep_ms(1000)
    

def ledClignote():
    oled.fill(0)
    oled.text("Blink LED", 0, 0)
    oled.show()
    led.value(1)
    sleep_ms(1000) 
    led.value(0)
    sleep_ms(1000)

def ledRGB():
    oled.fill(0)
    oled.text("RGB LED", 0, 0)
    oled.show()
    np[0] = (16, 0, 0)
    np.write()
    sleep_ms(1000)
    np[0] = (0, 16, 0)
    np.write()
    sleep_ms(1000)
    np[0] = (0, 0, 16)
    np.write()
    sleep_ms(1000)

def lm75():
    temp=str(sensorLm75.temp())
    print(temp)
    oled.fill(0)
    oled.text("LM75 sensor", 0, 0)
    oled.text(temp, 0, 10)
    oled.show()
    sleep_ms(100)
    
def ds18s20():
    ds.convert_temp()       
    sleep_ms(750)
    temp = str(ds.read_temp(sensorDs[0]))
    print(temp)
    oled.fill(0)
    oled.text("DS18S20 sensor", 0, 0)
    oled.text(temp, 0, 10)
    oled.show()
    sleep_ms(100)

def adcConvert():
    value=str(adc.read_u16()//64)
    print(value)
    oled.fill(0)
    oled.text("ADC", 0, 0)
    oled.text(value, 0, 10)
    oled.show()
    sleep_ms(100)
    

while True:
    try:
        if state==0:
            i2cScan()
        elif state==1:
            ledClignote()
        elif state==2:
            ledRGB()
        elif state==3:
            lm75()
        elif state==4:
            ds18s20()
        elif state==5:
            adcConvert()
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        sys.exit()

