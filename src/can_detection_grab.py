#!/usr/bin/env python3
# ---  ---  ---  ---  ---  ---
# file name:    can_detection_grab.py
# author:       CHEN Xiaosen
# date:         2024 01 07
# ---  ---  ---
# ---  ---  ---  ---  ---
# file name:         can_detection_grab.py
# description :      Once the target appears in the frame of the camera, the robot will go for it and grab it.
#
#
#
# author:            CHEN Xiaosen
# created on:        2024 01 07
# last updated:      2024 01 08
# updated by:        CHEN Xiaosen
# comment :          
# ---  ---   ---  ---  ---  ---

# ---  IMPORTS  ---  ---  ---  ---
from pixycamev3.pixy2 import *
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import *
from time import sleep
# ---  ---   ---  ---  ---  --



# Setup
us = UltrasonicSensor()
wheel_diameter=55.5
wheels = MoveTank(OUTPUT_A, OUTPUT_D)

# Use
# us.mode='US-DIST-CM'
distance = us.value()
# distance should be between 70 and 80

# Initialize the motors connected to the claw
claw_motor_right = MediumMotor(OUTPUT_B)

# Define functions to control the claw movement
def open_claw():
    #claw_motor_left.on_for_seconds(speed=50, seconds=1.5)
    claw_motor_right.on_for_seconds(speed=-50, seconds=1.5)

def close_claw():
    #claw_motor_left.on_for_seconds(speed=-50, seconds=1.5)
    claw_motor_right.on_for_seconds(speed=50, seconds=1.5)

def Straight ( speed ):
    wheels.on(speed, speed)
    
def turn_left ( speed ):
    wheels.on(0-speed, speed)

def turn_right ( speed ):
    wheels.on(speed, 0-speed)

def motor_stop():
    wheels.off()

# set port and i2c address
pixy2 = Pixy2(port=4, i2c_address=0x54)

# get version
version = pixy2.get_version()
print('Hardware: ', version.hardware)
print('Firmware: ', version.firmware)

# get frame resolution
resolution = pixy2.get_resolution()
print('Frame width: ', resolution.width)
print('Frame height: ', resolution.height)

# Turn upper leds on
pixy2.set_lamp(1, 0)
sleep(2)

# Track blocks with signature 1, request just 1 block wile true:
nr_blocks, blocks = pixy2.get_blocks(1, 1)

print('The number of the block is: ', nr_blocks)


if nr_blocks >= 1:
    sleep(10)
    try:
        while 1:
            nr_blocks, blocks = pixy2.get_blocks(1, 1)
            
            # I set this "if" beacause the camera is not stable. Sometimes the camera loses the target even the target is in the frame.
            if nr_blocks >= 1:
                x = blocks[0].x_center
            distance = us.value()
            print('The x-axis of the block is: ', x)
            print('The distance of the block is: ', distance)
            
            # The robot will first rotate to face the target， and then go grab the target.
            if 70<=distance<=80 and 100<=x<=200:
                motor_stop()
                # claw movement
                open_claw()
                sleep(2)
                close_claw()
                sleep(2)
                break
            elif x < 100:
                turn_right(10)
            elif x > 200:
                turn_left(10)
            elif 100<x<200 and distance < 70:
                Straight (-10)
            else:
                Straight (10)

    except KeyboardInterrupt:
        # Stop motors and exit cleanly on Ctrl+C
        #claw_motor_left.off()
        claw_motor_right.off()

# Turn upper leds off
pixy2.set_lamp(0, 0)
