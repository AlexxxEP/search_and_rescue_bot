# ---  ---  ---
# file name:    main.py
# author:      Alexandre MENSAH
# date:        2023 11 27
# ---  ---  ---

# Hello
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor,GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color 
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.robotics import DriveBase
    

ev3= EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track = 104)

while robot.distance() < 1500:
    robot.drive(500,0)
robot.stop()
left_motor.brake()
right_motor.brake()
wait(1000)
robot.turn(200)
while robot.distance() < 1200:
    robot.drive(500,0)
robot.stop()
left_motor.brake()
right_motor.brake()
wait(1000)
robot.turn(200)

while robot.distance() < 1000:
    robot.drive(500,0)
robot.stop()
left_motor.brake()
right_motor.brake()
wait(1000)
robot.turn(200)

while robot.distance() < 800:
    robot.drive(500,0)
robot.stop()
left_motor.brake()
right_motor.brake()
wait(1000)
robot.turn(200)
