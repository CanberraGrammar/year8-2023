from machine import Pin 
import time 
trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)
redPin = Pin(11,Pin.OUT)
yellowPin = Pin(12,Pin.OUT)
greenPin = Pin(13,Pin.OUT)
def measureUltrasonic():
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    while echo.value() == 0:
        startTime = time.ticks_us()
    while echo.value() == 1:
        finishTime = time.ticks_us()
    timepassed = finishTime - startTime
    distance = (timepassed / 2) * 0.0343
    return distance
while True:
    distance = measureUltrasonic()
    if distance <= 5:
        redPin.on()
        yellowPin.on()
        greenPin.on()
    elif distance <= 10:
        redPin.off()
        yellowPin.on()
        greenPin.on()
    elif distance <= 15:
        redPin.off()
        yellowPin.off()
        greenPin.on()
    else:
        redPin.off()
        yellowPin.off()
        greenPin.off()
    print(str(measureUltrasonic()) + "cm")
    time.sleep_ms(10)
