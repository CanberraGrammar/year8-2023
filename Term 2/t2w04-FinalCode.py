from machine import *
import time

def getFrequency(note):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    
    if len(note) == 3:
        octave = int(note[2])
    else:
        octave = int(note[1])

    keyNumber = int(notes.index(note[:-1]))

    if keyNumber < 3:
        keyNumber = keyNumber + 12 + ((octave - 1) * 12) + 1
    else:
        keyNumber = keyNumber + (octave - 1) * 12 + 1

    return int(440 * (2 ** ((keyNumber - 49) / 12)))

def playTune(tune,tempo,buzz):
    for note in tune:
        key, length = note
        if key == "R":
            buzz.duty_u16(0)
        else:
            buzz.duty_u16(int(0.5 * 65536))
            freq = getFrequency(key)
            buzz.freq(freq)
        time.sleep(60/tempo*length)
    buzz.duty_u16(0)

pot = ADC(Pin(26))
buzz = PWM(Pin(11))

buzz.freq(440)
buzz.duty_u16(int(0.5 * 65536))

notes = ["C4","D4","E4","F4","G4","A4","B4","C5"]

while True:
    reading = pot.read_u16()
    index = int(reading/(65536/len(notes)))
    note = notes[index]
    frequency = getFrequency(note)
    buzz.freq(frequency)
    print(reading,note)
    time.sleep(0.1)
