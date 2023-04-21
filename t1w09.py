from machine import *
from time import *

# Our own cobbled-together brightness code
"""
LEDStatic = Pin(1, Pin.OUT)
LEDStatic.on()
LED = Pin(0, Pin.OUT)
while True:
    LED.on()
    sleep_ms(1) 
    LED.off()
    sleep_ms(10)
"""

LEDStatic = Pin(1, Pin.OUT)
LEDStatic.on()

LED = PWM(Pin(0))
LED.freq(1000)

# Set a constant brightness
# LED.duty_u16(0.5 * 65536)

# Animate a triangle wave (arcsin (sin x))
"""
while True:
    # 65535 = 2^16 - 1
    for duty in range(65535):
        LED.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65535, 0, -1):
        LED.duty_u16(duty)
        sleep(0.0001)
"""

# Buttons to increase/decrease brightness
btnDwn = Pin(4, Pin.IN, Pin.PULL_UP)
btnUp = Pin(5, Pin.IN, Pin.PULL_UP)

duty = 0

# This allows for overflowing the LED since 
# duty of -1 is very bright, and duty of
# 65540 is very dim. Add duty <= 65035 and 
# duty >= 500 as guards.
while True:
    if btnUp.value() == 0:
        duty = duty + 500
        LED.duty_u16(duty)
    if btnDwn.value() == 0:
        duty = duty - 500
        LED.duty_u16(duty)
    print(duty)
    sleep_ms(10)