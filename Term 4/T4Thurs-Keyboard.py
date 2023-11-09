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

selectedPosition = (0, 0)

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

def drawKeyboard():
    for y in range(len(keyboard)):
        keyboardRow = keyboard[y]
        for x in range(len(keyboardRow)):
            c = keyboardRow[x]
            
            if selectedPosition == (x, y):
                oled.fill_rect(12 * x + 4, 12 * y + 8, 12, 12, 1)
                oled.rect(12 * x + 4, 12 * y + 8, 12, 12, 0)
                oled.text(c, 12 * x + 6, 12 * y + 10, 0)
            else:
                oled.rect(12 * x + 4, 12 * y + 8, 12, 12, 1)
                oled.text(c, 12 * x + 6, 12 * y + 10, 1)

def checkForMovement():
    move = readMove()
    
    global readyForNextMove
    global selectedPosition
    
    if (not readyForNextMove) and move == "M":
        readyForNextMove = True
    elif (readyForNextMove):
        x, y = selectedPosition
        if move == "U":
            selectedPosition = (x, y - 1)
            readyForNextMove = False
        elif move == "R":
            selectedPosition = (x + 1, y)
            readyForNextMove = False
        elif move == "L":
            selectedPosition = (x - 1, y)
            readyForNextMove = False
        elif move == "D":
            selectedPosition = (x, y + 1)
            readyForNextMove = False
        elif move == "P":
            c = keyboard[y][x]
            transmit(c)
            readyForNextMove = False
        selectedPosition = (selectedPosition[0] % len(keyboard[0]), selectedPosition[1] % len(keyboard))

def transmit(charToTransmit):
    # Transmit this character!
    print(charToTransmit)

while True:
    checkForMovement()
    oled.fill(0)
    drawKeyboard()
    oled.show()
    time.sleep_ms(10)
