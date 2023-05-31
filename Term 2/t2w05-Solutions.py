from machine import *
from ssd1306 import SSD1306_I2C
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)

# Name
oled.text('<Name>',40, 28, 1)

# Star
oled.line(64, 10, 80, 54, 1)
oled.line(80, 54, 30, 25, 1)
oled.line(30, 25, 98, 25, 1)
oled.line(98, 25, 48, 54, 1)
oled.line(48, 54, 64, 10, 1)

# Stripes
for x in range(0,8):
    oled.fill_rect(x*16,0,8,64,1)

# Slope
for y in range(0,63):
    width = y * 2
    oled.hline(0,y,width,1)

# Triangle
for y in range(0,63):
    x = 64-y
    length = y*2
    oled.hline(x,y,length,1)
    
# Fancy name
oled.fill_rect(24, 20, 80, 24, 1) # x y width height colour
oled.text('Hello', 44, 20, 0) # text x y colour
oled.text('My name is', 24, 28, 0) # text x y colour
oled.text('<Name>', 40, 36, 0) # text x y colour

# Circle
for y in range(0,63):
    x = int(64 - math.sqrt(32**2-(y-32)**(2)))
    length = int(2 * math.sqrt(32**2-(y-32)**(2)))
    oled.hline(x,y,length,1)

oled.show()
