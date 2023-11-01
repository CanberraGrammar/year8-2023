from machine import *
from ssd1306_plus import *
from random import *
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_PLUS(128, 64, i2c)

joyX = ADC(Pin(26))
joyY = ADC(Pin(27))
joyBtn = Pin(16,Pin.IN,Pin.PULL_UP)

def readMove():
    readingX = joyX.read_u16()/32768-1
    readingY = joyY.read_u16()/32768-1
    
    move = "M"
    if abs(readingX) > abs(readingY):
        if readingX > 0.95:
            move = "L"
        elif readingX < -0.95:
            move = "R"
    else:
        if readingY > 0.95:
            move = "D"
        elif readingY < -0.95:
            move = "U"
    if joyBtn.value() == 0:
        move = "P"
    return move

readyForNextMove = True

def checkForMovement():
    move = readMove()
    
    global readyForNextMove
    
    if (not readyForNextMove) and move == "M":
        readyForNextMove = True
    elif (readyForNextMove):
        if move == "U":
            pass
        elif move == "R":
            pass
        elif move == "L":
            pass
        elif move == "D":
            pass
        elif mode == "P":
            pass











