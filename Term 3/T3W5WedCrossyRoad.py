from machine import *
from ssd1306_plus import *
from random import *
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_PLUS(128, 64, i2c)

joyX = ADC(Pin(26))
joyY = ADC(Pin(27))
joyBtn = Pin(16,Pin.IN,Pin.PULL_UP)

playerX = 56
playerWidth = 16

def readMove():
    readingX = joyX.read_u16()/32768-1
    readingY = joyY.read_u16()/32768-1
    
    move = "M"
    if abs(readingX) > abs(readingY):
        if readingX > 0.95:
            move = "R"
        elif readingX < -0.95:
            move = "L"
    else:
        if readingY > 0.95:
            move = "U"
        elif readingY < -0.95:
            move = "D"
    return move

class Level():
    def __init__(self):
        self.speed = random() * 3 - 1.5
        self.width = randint(5,26)
        self.obstacles = list(range(0,128,self.width*3))
    
    def drawLevel(self,y):
        for x in self.obstacles:
            oled.fill_rect(int(x),int(y+1),(self.width),14,1)
    
    def update(self):
        for x in range(len(self.obstacles)):
            self.obstacles[x] += self.speed
            self.obstacles[x] = self.obstacles[x] % 128
    
    def isColliding(self):
        for x in self.objects:
            if (playerX + playerWidth > x and playerX < x + self.width):
                return True
        return False

game = []

def newGame():
    for i in range(4):
        game.append(Level())

def drawGame():
    oled.fill(0)
    for i in range(len(game)):
        game[i].drawLevel(i*16)
    oled.fill_rect(playerX,48,playerWidth,16,1)
    oled.show()

def updateGame():
    for i in range(len(game)):
        game[i].update()

newGame()
drawGame()

while True:
    updateGame()
    drawGame()
    time.sleep_ms(20)

