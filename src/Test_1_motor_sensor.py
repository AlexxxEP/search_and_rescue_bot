#!/usr/bin/env python3

# An EV3 Python (library v2) solution to Exercise 3
# of the official Lego Robot Educator lessons that
# are part of the EV3 education software

from ev3dev2.motor import LargeMotor
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from time import sleep

btn = Button() # we will use any button to stop script

lm = LargeMotor()

while not btn.any():    # exit loop when any button pressed

        lm.on_for_seconds(50, 3)
        sleep(1)
