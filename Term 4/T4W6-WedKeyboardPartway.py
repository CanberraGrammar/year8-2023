from machine import *
from ssd1306_plus import *
from random import *
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_PLUS(128, 64, i2c)

joyX = ADC(Pin(26))
joyY = ADC(Pin(27))
joyBtn = Pin(16,Pin.IN,Pin.PULL_UP)

keyboard = [
    "1234567890",
    "ABCDEFGHIJ",
    "KLMNOPQRST",
    "UVWXYZ .!?"
    ]

selected = (0,0)


output = Pin(15, Pin.OUT)

def transmit(char):
    unit = 0.05
    
    number = ord(char)
    len4 = int(number/64)
    number -= len4*64
    len3 = int(number/16)
    number -= len3*16
    len2 = int(number/4)
    number -= len2*4
    len1 = number
    
    for i in range(len4):
        output.value(1)
        time.sleep(4*unit)
        output.value(0)
        time.sleep(unit)
    
    for i in range(len3):
        output.value(1)
        time.sleep(3*unit)
        output.value(0)
        time.sleep(unit)
    
    for i in range(len2):
        output.value(1)
        time.sleep(2*unit)
        output.value(0)
        time.sleep(unit)
    
    for i in range(len1):
        output.value(1)
        time.sleep(unit)
        output.value(0)
        time.sleep(unit)
    
    time.sleep(unit)

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
    
    global readyForNextMove, selected
    
    if (not readyForNextMove) and move == "M":
        readyForNextMove = True
    elif (readyForNextMove):
        selX, selY = selected
        if move == "U":
            selected = (selX, selY + 1)
            readyForNextMove = False
        elif move == "R":
            selected = (selX + 1, selY)
            readyForNextMove = False
        elif move == "L":
            selected = (selX - 1, selY)
            readyForNextMove = False
        elif move == "D":
            selected = (selX, selY - 1)
            readyForNextMove = False
        elif move == "P":
            transmit(keyboard[selX][selY])
            readyForNextMove = False
        selX = selX % 10
        selY = selY % 4

def drawKeyboard():
    for y in range(len(keyboard)):
        for x in range(len(keyboard[y])):
            if selected == (x,y):
                oled.fill_rect(x*12,y*12,12,12,1)
                oled.rect(x*12,y*12,12,12,0)
                oled.text(keyboard[y][x],x*12+2,y*12+2,0)
            else:
                oled.rect(x*12,y*12,12,12,1)
                oled.text(keyboard[y][x],x*12+2,y*12+2,1)

while True:
    checkForMovement()
    oled.fill(0)
    drawKeyboard()
    oled.show()
    time.sleep_ms(10)
