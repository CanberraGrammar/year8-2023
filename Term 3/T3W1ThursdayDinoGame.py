from machine import *
from ssd1306 import SSD1306_I2C
from random import *
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

btnJump = Pin(2, Pin.IN, Pin.PULL_UP)
btnDuck = Pin(3, Pin.IN, Pin.PULL_UP)

floorY = 56

dinoX = 24
dinoY = floorY
dinoVY = 0
dinoAY = 0.3
dinoWidth = 13
dinoHeight = 22

while True:
    startTime = time.ticks_ms()
    oled.fill(0)

    #Floor
    oled.hline(0,floorY,128,1)
    
    #Dino
    if btnDuck.value() == 0:
        dinoWidth = 22
        dinoHeight = 13
        dinoAY = 0.4
    else:
        dinoWidth = 13
        dinoHeight = 22
        dinoAY = 0.013
    dinoY = min(dinoY + dinoVY,floorY)
    if btnJump.value() == 0 and dinoY == floorY:
        dinoVY = -0.88
    dinoVY = dinoVY + dinoAY
    oled.fill_rect(dinoX,int(dinoY-dinoHeight),dinoWidth,dinoHeight,1)
    
    oled.show()
    endTime = time.ticks_ms()
    time.sleep_ms(50 - (endTime - startTime))
