from machine import *
from ssd1306_plus import *
from random import *
import time

inputPin = Pin(0, Pin.IN, Pin.PULL_DOWN)

index = 0

unit = 0.05

while True:
    currentValue = inputPin.value()
    startTime = time.ticks_ms()

    while inputPin.value() == currentValue:
        time.sleep_ms(10)
    endTime = time.ticks_ms()
    difference = round((endTime - startTime)/1000/unit)
    if currentValue == 1 and difference == 1:
        index += 1
    if currentValue == 1 and difference == 2:
        index += 4
    if currentValue == 1 and difference == 3:
        index += 16
    if currentValue == 1 and difference == 4:
        index += 64
    if currentValue == 0 and difference == 2:
        char = chr(index)
        print(char)
        index = 0