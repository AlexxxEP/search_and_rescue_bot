# ---  ---  ---  ---  ---
# file name:         Test_2_ColorStop
# description :      The robot will go forward until the color sensor detects black color
#
#
#
# author:            Alexandre MENSAH
# created on:        2023 12 04
# last updated:      
# updated by:        
# comment :          
# ---  ---   ---  ---  ---  ---
#!/usr/bin/env python3
# ---  ---  ---  ---  ---  ---

# ---  IMPORTS  ---  ---  ---  ---
from ev3dev2.motor import LargeMotor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from time import sleep
# ---  ---   ---  ---  ---  ---

# ---  DECLARATIONS  ---
btn = Button() # we will use any button to stop script
lm = LargeMotor()
mt = MoveTank(OUTPUT_B, OUTPUT_C)
cl = ColorSensor()
# ---  ---  ---  ---  ---  ---

# ---  CODE START  ---
while not btn.any():    # exit loop when any button pressed
    if cl.color != 1 :
        mt.on(50)
    else
        mt.off()

    sleep(1)
# ---  ---  ---  ---  ---  ---
