#!/usr/bin/env python3
# ---  ---  ---  ---  ---
# file name:         movement.py
# description :		 handles the movement of the robot
#
# author:            Alexandre EANG
# created on:        2023 12 31
# last updated:      2023 12 31
# updated by:        Alexandre EANG
# comment :          * Created file
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
# ---  ---  ---  ---  ---  ---



# ---  FUNCTION DEFINITION  ---

#	--- INITIALIZATION FUNCTION
def init(*args):
	"""
	init of movement submodules
	"""
	global PERIPH
	try:
		PERIPH = args[0]
		print(PERIPH)
		module_init = True
	except:
		print("\n\t>>> Failed to call PERIPH from {}".format(__name__))
		return 1
	return


#	--- BASIC FUNCTIONS
def straight(speed=15, use_gyro=False):
	"""
	Runs straight following the facing angle
	if no angle is specified, then the robot shall
	run without gyroscope handling
	The latter option shall only be used when 
	position tracking is not required, such as
	calibration, manual movement, etc.
	"""
	if module_init != True :
		print("\n\t>>> Error : wheelset has not been instanciated to {}".format(__name__))
		return 1

	global PERIPH


	return

def stop():
	"""
	"""
	if module_init != True :
		print("\n\t>>> Error : wheelset has not been instanciated to {}".format(__name__))
		return 1

	global PERIPH

	

	return


#	--- COMPOUND FUNCTIONS


# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---
if __name__ == '__main__':
	print("Running movement.py")