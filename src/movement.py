#!/usr/bin/env python3
# ---  ---  ---  ---  ---
# file name:         movement.py
# description :		 handles the movement of the robot
#
# author:            Alexandre EANG
# created on:        2023 12 31
# last updated:      2024 01 09
# updated by:        Alexandre EANG
# comment :          * Added compound functions
# ---  ---   ---  ---  ---  ---
if (__name__ != '__main__'): print("# importing {}".format(__name__))



# ---  IMPORTS  ---  ---  ---
import math as m
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
# --- CONSTANTS / CONFIG
PERIPH =[]
module_init = False

# Constants for the robot's movements
wheel_diameter = 5.6 # Diameter of the wheels in centimeters
wheel_circumference = wheel_diameter * m.pi # Circumference = π * diameter
wheel_distance = 12.5 # Distance between the wheels in centimeters

wheel_trackdist = 15
wheel_trackcircumference = wheel_trackdist * m.pi
wheel_dist_to_travel = wheel_trackcircumference / 4
radian_to_travel = 2 * m.pi * wheel_dist_to_travel / wheel_circumference
degrees_to_travel = m.degrees(radian_to_travel)

# Calculate the number of rotations needed for the robot to move forward by 1.5 meters
# Distance traveled = Number of rotations * Wheel circumference
distance_to_travel = 150 # 1.5 meters = 150 centimeters
rotations_needed = distance_to_travel / wheel_circumference

# ---  ---  ---  ---  ---  ---



# ---  FUNCTION DEFINITION  ---

#	--- INITIALIZATION FUNCTION
def init(*args):
	"""
	init of movement submodule
	"""
	global PERIPH
	global SYS
	global module_init

	try:
		PERIPH = args[0]
		module_init = True
	except:
		print("\n\t>>> Failed to call PERIPH from {}".format(__name__))
		return 1
	try:
		SYS = args[1]
	except:
		print("\n\t>>> Failed to call SYS from {}".format(__name__))
		return 1
	return


#	--- BASIC FUNCTIONS
def straight(speed=15, use_gyro=False, follow_angle=0):
	"""
	Runs straight following the facing angle
	if no angle is specified, then the robot shall
	run without gyroscope handling
	The latter option shall only be used when 
	position tracking is not required, such as
	calibration, manual movement, etc.
	"""
	global PERIPH
	global straight_kp
	global straight_ki
	global straight_kd

	if module_init != True :
		print("\n\t>>> Error : wheelset has not been instanciated to {}".format(__name__))
		return 1
	if use_gyro:
		PERIPH["wheels"].follow_gyro_angle(straight_kp,straight_ki,straight_kd,8, follow_angle, 0.05,follow_for_ms, ms=1000)
	else:
		PERIPH["wheels"].on(speed, speed)

	return

def stop():
	"""
	"""
	if module_init != True :
		print("\n\t>>> Error : wheelset has not been instanciated to {}".format(__name__))
		return 1

	


	global PERIPH

	PERIPH["wheels"].on(0,0)
	

	return


#	--- COMPOUND FUNCTIONS



# Function to make the robot move forward by a given number of rotations
def move_forward():
	global PERIPH
	PERIPH["wheels"].left_motor.on_for_rotations(speed=20, rotations=rotations_needed)
	PERIPH["wheels"].right_motor.on_for_rotations(speed=20, rotations=rotations_needed)

# # Function to make the robot turn 90 degrees to the left
# def turn_left():
# 	global PERIPH
# 	PERIPH["wheels"].left_motor.on_for_rotations(speed=-20, rotations=rotations_needed / 4)
# 	PERIPH["wheels"].right_motor.on_for_rotations(speed=20, rotations=rotations_needed / 4)

# # Function to make the robot turn 90 degrees to the right
# def turn_right():
# 	global PERIPH
# 	PERIPH["wheels"].left_motor.on_for_rotations(speed=20, rotations=rotations_needed / 4)
# 	PERIPH["wheels"].right_motor.on_for_rotations(speed=-20, rotations=rotations_needed / 4)

# Function to make the robot turn 90 degrees to the left
def turn_left():
	global PERIPH
	PERIPH["wheels"].on_for_degrees(left_speed=20,right_speed=-20,  degrees=degrees_to_travel)
# Function to make the robot turn 90 degrees to the right
def turn_right():
	global PERIPH
	PERIPH["wheels"].on_for_degrees(left_speed=-20,right_speed=20, degrees=degrees_to_travel)


# def retracting_circle():
# 	try:
# 		global PERIPH
# 		# Explore the 1.5x1.5 meters square area using a retracting square pattern
# 		for _ in range(4): # Repeat the square pattern four times to cover the area
# 			move_forward()
# 			turn_left()
# 			move_forward()
# 			turn_right()

# 	except KeyboardInterrupt:
# 		global PERIPH
# 		# Stop motors and exit cleanly on Ctrl+C
# 		PERIPH["wheels"].left_motor.off()
# 		PERIPH["wheels"].right_motor.off()


# return


def retracting_circle():
	turn_right()
	return


# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---
if __name__ == '__main__':
	print("Running movement.py")