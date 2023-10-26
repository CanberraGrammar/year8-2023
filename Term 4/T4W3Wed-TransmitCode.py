from machine import *
from ssd1306_plus import *
from random import *
import time


output = Pin(0, Pin.OUT)

string = "cast"

unit = 0.05

while True:
    for char in string:
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

