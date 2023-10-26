from machine import *
import time

unit = 0.05

inputPin = Pin(0, Pin.IN, PULL_DOWN)

# buggy still

while True:
    c = 0
    
    currentValue = inputPin.value()
    startTime = time.ticks_ms()
    
    while inputPin.value() == currentValue:
        time.sleep_ms(10)
    
    endTime = time.ticks_ms()
    difference = round((endTime - startTime)/1000/unit)
    
    if currentValue == 1:
        if difference == 1:
            c += 1
        elif difference == 2:
            c += 2
        elif difference == 3:
            c += 4
        elif difference == 4:
            c += 8
        elif difference == 5:
            c += 16
    elif currentValue == 0 and difference == 2:
        char = chr(c)
        print(char)
        c = 0
