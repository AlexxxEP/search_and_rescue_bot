# ---  ---  ---  ---  ---
# file name:         Test_1_motor_sensor.py
# description :
#
#
#
# author:            Alexandre MENSAH
# created on:        2023 11 27
# last updated:      2023 11 28
# updated by:        Alexandre EANG
# comment :          * Added titleblock for document
#                    * Added code segments while spacing segments 3 lines apart
#                    * Please @alexandre_mensah fill the purpose of the script
#                    in the description block
# ---  ---   ---  ---  ---  ---
#!/usr/bin/env python3
# ---  ---  ---  ---  ---  ---



# ---  IMPORTS  ---  ---  ---  ---
from ev3dev2.motor import Motor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from time import sleep
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
btn = Button() # we will use any button to stop script

lm = Motor()

us = UltrasonicSensor()
# ---  ---  ---  ---  ---  ---



# ---  CODE START  ---
while not btn.any():    # exit loop when any button pressed

    if us.distance_centimeters < 40:

        lm.on(50)
        sleep(1)


# ---  ---  ---  ---  ---  ---



# ---  FUNCTION DEFINITION  ---
# ---  ---  ---  ---  ---  ---  ---
