from machine import *
from ssd1306 import SSD1306_I2C
from random import *
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

btnJump = Pin(2, Pin.IN, Pin.PULL_UP)
btnDuck = Pin(3, Pin.IN, Pin.PULL_UP)

floorY = 48.0

dinoX = 16
dinoY = floorY
dinoVY = 0
dinoAY = 0.15
dinoWidth = 8
dinoHeight = 16

while True:
    starttime = time.ticks_ms()
    oled.fill(0)

    #Floor
    oled.hline(0,int(floorY),128,1)

    #Dino
    if btnDuck.value() == 0 and dinoY == floorY:
        dinoHeight = 8
    else:
        dinoHeight = 16
    dinoY = min(dinoY + dinoVY, floorY)
    if dinoY == floorY:
        if btnJump.value() == 0:
            dinoVY = -3
        else:
            dinoVY = 0
    else:
        dinoVY = dinoVY + dinoAY
    oled.fill_rect(dinoX,int(dinoY-dinoHeight),dinoWidth,dinoHeight,1)

    oled.show()
    endtime = time.ticks_ms()
    time.sleep_ms(50 - (endtime - starttime))
