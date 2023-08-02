from machine import *
from ssd1306 import SSD1306_I2C
from random import *
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

btnJump = Pin(2, Pin.IN, Pin.PULL_UP)
btnDuck = Pin(3, Pin.IN, Pin.PULL_UP)


Buzz = PWM(Pin(4))

Buzz.freq(440)
Buzz.duty_u16(int(0 * 65536))


floorY = 48.0

dinoX = 16
dinoY = floorY
dinoVY = 0
dinoAY = 0.15
dinoWidth = 8
dinoHeight = 16

obstacles = [(64,40,8),(128,24,15)]

gameRunning = True

score = 0

isDucking = False

def getFrequency(note):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    
    if len(note) == 3:
        octave = int(note[2])
    else:
        octave = int(note[1])

    keyNumber = int(notes.index(note[:-1]))

    if keyNumber < 3:
        keyNumber = keyNumber + 12 + ((octave - 1) * 12) + 1
    else:
        keyNumber = keyNumber + (octave - 1) * 12 + 1

    return int(440 * (2 ** ((keyNumber - 49) / 12)))

def playTune(tune,tempo,buzz):
    for note in tune:
        key, length = note
        if key == "R":
            buzz.duty_u16(0)
        else:
            buzz.duty_u16(int(0.5 * 65536))
            freq = getFrequency(key)
            buzz.freq(freq)
        time.sleep(60/tempo*length)
    buzz.duty_u16(0)

while gameRunning:
    starttime = time.ticks_ms()
    oled.fill(0)

    #Floor
    oled.hline(0,int(floorY),128,1)

    #Dino
    Buzz.duty_u16(int(0 * 65536))
    if btnDuck.value() == 0 and dinoY == floorY:
        if not isDucking:
            Buzz.freq(330)
            Buzz.duty_u16(int(0.5 * 65536))
            isDucking = True
        dinoHeight = 8
    else:
        isDucking = False
        dinoHeight = 16
    dinoY = min(dinoY + dinoVY, floorY)
    if dinoY == floorY:
        if btnJump.value() == 0:
            dinoVY = -3
            Buzz.freq(660)
            Buzz.duty_u16(int(0.5 * 65536))
        else:
            dinoVY = 0
    else:
        dinoVY = dinoVY + dinoAY
    oled.fill_rect(dinoX,int(dinoY-dinoHeight),dinoWidth,dinoHeight,1)
    
    #Obstacles
    for i in range(len(obstacles)):
        obstX, obstY, obstSize = obstacles[i]
        obstX -= 1
        if obstX <= 0 - obstSize:
            obstX = 128
            obstSize = randint(5,12)
            obstY = randint(0,int(floorY-obstSize))
        
        if (obstX < dinoX + dinoWidth and obstX + obstSize > dinoX and obstY < dinoY and obstY + obstSize > dinoY - dinoHeight):
            gameRunning = False

        obstacles[i] = (obstX, obstY, obstSize)
        oled.fill_rect(obstX,obstY,obstSize,obstSize,1)
    
    score += 10
    oled.text(str(score),128-len(str(score))*8,57)
    
    oled.show()    
    endtime = time.ticks_ms()
    time.sleep_ms(30 - (endtime - starttime))
 
oled.fill(0)
oled.text("Game Over",28,28,1)
oled.text("Score: " + str(score),64-len("Score: " + str(score))*4,36)
oled.show()
playTune([("G4",1),("D4",1),("G3",2)],90,Buzz)
