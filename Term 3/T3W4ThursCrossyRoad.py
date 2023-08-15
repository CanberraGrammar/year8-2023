from machine import *
from ssd1306_plus import *
from random import *
 
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = SSD1306_PLUS(128, 64, i2c)
 
joyX = ADC(Pin(26))
joyY = ADC(Pin(27))
joyBtn = Pin(16, Pin.IN, Pin.PULL_UP)
 
def getJoystickMove():
    readingX = joyX.read_u16()/32768 - 1
    readingY = joyY.read_u16()/32768 - 1
    direction = "middle"
 
    if abs(readingX) > abs(readingY):
        if readingX > 0.95:
            direction = "right"
        elif readingX < -0.95:
            direction = "left"
    else:
        if readingY > 0.95:
            direction = "up"
        elif readingY < -0.95:
            direction = "down"
 
    print(direction)
 
    return direction
 
class Level:
    def __init__(self, style="default"):
        if randint(0, 2) == 0:
            self.objects = []
            self.width = 0.0
            self.speed = 0.0
        else:
            self.speed = choice([1, -1]) * (random() + 0.5)
            self.width = 14 + (random() * 14)
            self.objects = list(range(0, 128, int(self.width * 4)))
 
    def update(self):
        for i in range(len(self.objects)):
            self.objects[i] += self.speed
            self.objects[i] = ((self.objects[i] + self.width) % (128 + self.width)) - self.width
 
    def drawLevel(self, y):
        for obj in self.objects:
            oled.fill_rect(int(obj), int(y + 1), int(self.width), 14, 1)
 