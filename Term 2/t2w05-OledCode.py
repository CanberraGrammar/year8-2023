from machine import *
from ssd1306 import SSD1306_I2C
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0) # colour
oled.pixel(10, 0, 1) #x y colour

oled.hline(0, 8, 4, 1) #x y length colour
oled.vline(0, 8, 4, 1) #x y length colour
oled.line(0, 0, 127, 63, 1) #x start, y start, x end, y end colour

oled.rect(10, 10, 107, 43, 1) #x y width height colour
oled.fill_rect(10, 10, 107, 43, 1) # x y width height colour
oled.text('Hello World', 0, 0, 1) # text x y colour

oled.show()