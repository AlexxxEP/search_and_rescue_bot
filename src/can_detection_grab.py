from pixycamev3.pixy2 import *
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import MediumMotor, OUTPUT_A
from time import sleep



# Setup
us = UltrasonicSensor()

# Use
us.mode='US-DIST-CM'
distance = us.value()
# distance should be between 70 and 80

# Initialize the motors connected to the claw
claw_motor_right = MediumMotor(OUTPUT_A)

# Define functions to control the claw movement
def open_claw():
    #claw_motor_left.on_for_seconds(speed=50, seconds=1)
    claw_motor_right.on_for_seconds(speed=-50, seconds=1)

def close_claw():
    #claw_motor_left.on_for_seconds(speed=-50, seconds=1)
    claw_motor_right.on_for_seconds(speed=50, seconds=1)


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

# Turn upper leds on for 2s, then turn off
pixy2.set_lamp(1, 0)


# Track blocks with signature 1, request just 1 block wile true:
nr_blocks, blocks = pixy2.get_blocks(1, 1)

if nr_blocks >= 1:
    sig = blocks[0].sig
    x = blocks[0].x_center
    y = blocks[0].y_center
    w = blocks[0].width
    h = blocks[0].height
    sleep(10)
    try:
        while True:
            print('The x-axis of the block is: ', x)
            print('The distance of the block is: ', distance)
            if 70<distance<80 and 100<x<200:
            # claw movement
                close_claw()
                sleep(2)
                open_claw()
                sleep(2)
    except KeyboardInterrupt:
        # Stop motors and exit cleanly on Ctrl+C
        #claw_motor_left.off()
        claw_motor_right.off()

pixy2.set_lamp(0, 0)
