#!/usr/bin/env python3
# ---  ---  ---  ---  ---  ---
# file name:    main.py
# author:       Alexandre EANG
# date:         2023 12 11
# ---  ---  ---
# ---  ---  ---  ---  ---
# file name:         SquarePattern.py
# description :      Movement plus rectracting square pattern
#
#
#
# author:            Alexandre EANG
# created on:        2023 12 11
# last updated:      2023 12 11
# updated by:        Alexandre EANG
# comment :          * Applied template to this document
# ---  ---   ---  ---  ---  ---



# ---  IMPORTS  ---  ---  ---  ---
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from time import sleep
# ---  ---   ---  ---  ---  --



# ---  DECLARATIONS  ---
    # --- CONSTANTS
wheel_diameter=55.5
color = ColorSensor()
wheels = MoveTank( OUTPUT_D, OUTPUT_A)
gyro = GyroSensor()
wheels.gyro = GyroSensor()
timeout = 3000
    # --- VARIABLES
current_ang= 0
timecount = 0




# ---  FUNCTION DEFINITION  ---
# write function definitions here
# ---  ---  ---  ---  ---  ---  ---
def Straight ( speed ):
    wheels.on(speed, speed)
    return

def Pivot(direction ="cw", angle= 90):
    current_ang = gyro.angle
    timecounter = 0

    if (direction == "cw"):
        while (current_ang +angle >= gyro.angle ):
            timecounter +=1
            if(timecounter == timeout):
                break

            wheels.on(10, -10)
        Stop()
        return 0
    elif (direction == "ccw"):
         while (current_ang - angle <= gyro.angle):
            if(timecounter == timeout):
                break
            timecounter +=1

            wheels.on(-10, 10)
         Stop()
         return 0

    else:
      print("specify cw or ccw")
    return 1

def PivotPID(angle= 90, speed=10, kp=0, ki=0, kd=0):
    current_ang = gyro.angle
    timecounter = 0
    pid_speed = speed
    old_pid_speed = speed

    if (angle == 0):
        return 1


    elif (angle > 0):
        while (current_ang +angle >= gyro.angle ):
            timecounter +=1
            if(timecounter == timeout):
                print("Timed out")
                return 1
            ang_delta = current_ang +angle - gyro.angle
            print("ang_delta", ang_delta)
            pid_speed = (ang_delta/angle) * kp  
            pid_speed -= (pid_speed - old_pid_speed) * ki
            print("pid_speed", pid_speed)
            old_pid_speed = pid_speed
            print("old_pid_speed", old_pid_speed)
            pid_speed_percent = pid_speed //100
            wheels.on(pid_speed_percent, -pid_speed_percent)
        Stop()
        return 0


    elif (angle < 0):
         while (current_ang - angle <= gyro.angle):
            timecounter +=1
            if(timecounter == timeout):
                print("Timed out")
                return 1
            

            ang_delta = current_ang +angle - gyro.angle

            effective_speed = speed + (ang_delta* kp) - (speed*kd)

            wheels.on(effective_speed, -effective_speed)
         Stop()
         return 0



    else:
      print("specify cw or ccw")
    return 1


def Turn(direction):
    current_ang = gyro.angle
    print(current_ang)
    timecounter = 0
    if (direction == "cw"):
        while (current_ang +180 >= gyro.angle ):
            timecounter +=1
            print(gyro.angle)
            wheels.on(10, 0)
            if(timecounter == timeout):
                break
        Stop()
        return
    elif (direction == "ccw"):
         while (current_ang - 180 <= gyro.angle):
             timecounter +=1
             print(gyro.angle)
             wheels.on(0, 10)
             if(timecounter == timeout):
                break
         Stop()
         return
    else:
      print("specify cw or ccw")
    return


def Stop (  ):
    wheels.on(0, 0)
    return





# ---  CODE START  ---
print("Hello, World!")
print("Init: DO NOT MOVE")
wheels.gyro.calibrate()
color.calibrate_white()
print("Init: done, starting soon ...")

# try:
#     wheels.follow_gyro_angle(
#                     kp=11.3, ki=0.05, kd=3.2,
#                     speed=20,
#                     target_angle=45
#                 )
# except FollowGyroAngleErrorTooFast:
#     Stop()
#     raise

#---  CODE TEST DEF START  ---
def QuarterTurns( speed = 30, direction = "cw"):
    timecount = 0

    Straight(speed)
    while (True):
      timecount +=1
      if ( timecount == timeout):
        Stop()
        return

      if (color.color == 1):
            print("found edge")
            Stop()
            print("turning now")
            Turn(direction)
            QuarterTurns(speed, direction)
    return


Stop()