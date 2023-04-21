from machine import *
from time import *

LED = PWM(Pin(0))
LED.freq(1000)

# One-player reaction game
"""
btnGreen = Pin(5, Pin.IN, Pin.PULL_UP)
duty = 0
change = 1
while True:
    if duty >= 65535:
        change = -1
    if duty <= 0:
        change = 1
    duty = duty + change
    LED.duty_u16(duty)
    if btnGreen.value() == 0:
        print("Your score is: " + str(duty))
        sleep(1)
    sleep(0.0001)
"""

# Two-player reaction game
player1Btn = Pin(5, Pin.IN, Pin.PULL_UP)
player2Btn = Pin(4, Pin.IN, Pin.PULL_UP)

duty = 0
change = 1

player1Score = -1
player2Score = -1

while True:
    if duty >= 65535:
        change = -1
        player1Score = -1
        player2Score = -1

    if duty <= 0:
        change = 1

    duty = duty + change
    LED.duty_u16(duty)

    if player1Btn.value() == 0:
        player1Score = duty

    if player2Btn.value() == 0:
        player2Score = duty

    if (player1Score != -1) and (player2Score != -1):
        print("Your player1 score is: " + str(player1Score))
        print("Your player2 score is: " + str(player2Score))

        if (player1Score > player2Score):
            print("Player 2 Wins")
        else:
            print("Player 1 Wins")

        sleep(1)
        player1Score = -1
        player2Score = -1

    sleep(0.0001)