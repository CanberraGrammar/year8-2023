from machine import *
from ssd1306_plus import *
from random import *
import time


output = Pin(25, Pin.OUT)

string = "cast"

for char in string:
    number = ord(char) - 96
    long = int(number/10)
    short = number % 10
    
    for i in range(long):
        output.value(1)
        time.sleep(3)
        output.value(0)
        time.sleep(1)
    
    for i in range(short):
        output.value(1)
        time.sleep(1)
        output.value(0)
        time.sleep(1)
    
    time.sleep(5)
