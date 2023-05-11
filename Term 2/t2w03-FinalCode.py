from machine import *
import time

Buzz = PWM(Pin(11))

def playTune(tune, tempo):
    Buzz.duty_u16(int(0.5 * 65536))
    for note in tune:
        key, length = note
        if key == "R":
            Buzz.duty_u16(0)
            time.sleep(length*60/tempo)
            Buzz.duty_u16(int(0.5 * 65536))
        else:
            Buzz.freq(getFrequency(key))
            time.sleep(length*60/tempo)
    Buzz.duty_u16(0)

tune = [("C4",1),("D4",0.5),("E4",0.5),("R",1),("F4",0.5),("G4",0.5)]
tempo = 60

playTune(tune, tempo)