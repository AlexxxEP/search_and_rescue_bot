#!/usr/bin/env python3

# An EV3 Python (library v2) solution to Exercise 3

# of the official Lego Robot Educator lessons that

# are part of the EV3 education software

from ev3dev2.motor import Motor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from time import sleep

btn = Button() # we will use any button to stop script

lm = Motor()

us = UltrasonicSensor()

while not btn.any():    # exit loop when any button pressed

    if us.distance_centimeters < 40:

        lm.on(50)
        sleep(1)
