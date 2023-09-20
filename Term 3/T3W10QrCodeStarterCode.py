from machine import *
from ssd1306_plus import *
from random import *
import time
import micropython_qr as qrcode

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_PLUS(128, 64, i2c)
qr = qrcode.QRCode(
    box_size=1,
    border=0,
)