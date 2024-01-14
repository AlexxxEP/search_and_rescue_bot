#!/usr/bin/env python3
# ---  ---  ---  ---  ---
# file name:         sensors.py
# description :		 handles robot sensors
#
# author:            Alexandre EANG
# created on:        2024 01 14
# last updated:      2024 01 14
# updated by:        Alexandre EANG
# comment :          * Created file
# ---  ---   ---  ---  ---  ---
if (__name__ != '__main__'): print("# importing {}".format(__name__))



# ---  IMPORTS  ---  ---  ---
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
# --- CONSTANTS / CONFIG
PERIPH =[]
SYS =[]
module_init = False



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
def poll_sonar(threshold_cm=20, poll_iteration_threshold = 200):
	"""
	check if an object is within a certain distance of the robot
	"""
	if module_init != True :
		print("\n\t>>> Error : wheelset has not been instanciated to {}".format(__name__))
		return 1

	global PERIPH
	global sonar_detected
	global sonar_enable

	poll_iterator = 0

	while sonar_enable:
		poll_iterator += 1
		if poll_iterator == poll_iteration_threshold:
			sonar_detected = sonar_evaluate(threshold_cm)
			poll_iterator = 0
	return

def sonar_evaluate(threshold_cm=20):
	"""
	returns true if an object is detected below specified threshold
	return false otherwise
	"""
	global PERIPH
	try:
		distance_cm = PERIPH["sonar"].distance_centimeters
	except:
		return False
		
	if PERIPH["sonar"].distance_centimeters <= threshold_cm:
		return True
	else:
		return False

# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---
if __name__ == '__main__':
	print("Running sensors.py")