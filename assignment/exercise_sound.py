#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""


import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

#              A    C       D       D       D       E       F       F       F       G    E       E      D       C      C        D
freq = [220, 261.6, 293.66, 293.66, 293.66, 329.63, 349.23, 349.23, 349.23, 392, 329.63, 329.63, 293.66, 261.6, 261.6, 293.66]
duration = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 3]  # seconds

for i in range(len(duration)):
    duration[i] *= 0.15

duration = duration

print("Playing frequency (Hz):")

for i in range(len(duration)):
    print(freq[i])
    playtone(int(freq[i]), duration[i])

# Turn off the PWM
quiet()
