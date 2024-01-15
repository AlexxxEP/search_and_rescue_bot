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
SYS =[]
module_init = False

straight_kp = 10
straight_ki = 0
straight_kd = 0.8

adj_length = 0
A_dist = 0
B_dist = 0
C_dist = 0
D_dist = 0

hairpin_tol = 0 # tacho counts

turning_tolerance_left= 8 #degrees
turning_tolerance_right= 6 #degrees
wheel_diameter = 5.6 # Diameter of the wheels in centimeters
wheel_circumference = wheel_diameter * m.pi # Circumference = π * diameter
wheel_trackdist = 11.8

pivot_circumference = wheel_trackdist * m.pi
pivot_quarterturndistance = pivot_circumference / 4

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
	global straight_kp
	global straight_ki
	global straight_kd

	try:
		PERIPH = args[0]
		module_init = True
	except:
		print("\n\t>>> Failed to call PERIPH from {}".format(__name__))
		return 1
	try:
		SYS = args[1]
		straight_kp = SYS["logic_kp"]
		straight_ki = SYS["logic_ki"]
		straight_kd = SYS["logic_kd"]
	except:
		print("\n\t>>> Failed to call SYS from {}".format(__name__))
		return 1
	return


#	--- BASIC FUNCTIONS
def straight(speed=25, use_gyro=False, follow_angle=0):
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

def turn_left(method = 'gyro'):
	global PERIPH

	degrees_to_travel = m.degrees(2 * m.pi * pivot_quarterturndistance / wheel_circumference)

	if method == 'gyro':
			start_angle = PERIPH["wheels"].gyro.angle
			target_angle = start_angle - 90
			speed = 15

			while (abs(target_angle - PERIPH["wheels"].gyro.angle)) > turning_tolerance_left:
				PERIPH["wheels"].on(-speed, speed)

			stop()
	else:
		PERIPH["wheels"].on_for_degrees(left_speed=20,right_speed=-20,  degrees=degrees_to_travel)
	return

def turn_right(method = 'gyro'):
	global PERIPH

	degrees_to_travel = m.degrees(2 * m.pi * pivot_quarterturndistance / wheel_circumference)

	if method == 'gyro':
			start_angle = PERIPH["wheels"].gyro.angle
			target_angle = start_angle + 90
			speed = 15

			while (abs(target_angle - PERIPH["wheels"].gyro.angle)) > turning_tolerance_right:
				PERIPH["wheels"].on(speed, -speed)

			stop()
	else:
		PERIPH["wheels"].on_for_degrees(left_speed=20,right_speed=-20,  degrees=degrees_to_travel)
	return

def open_claw():
    PERIPH["claw"].on_for_seconds(speed=50, seconds=1)
    return

def close_claw():
    PERIPH["claw"].on_for_seconds(speed=-50, seconds=1)
    return



#	--- COMPOUND FUNCTIONS

def halfturn_right(direction=''):
	"""
	makes a U turn clockwise
	"""
	global PERIPH
	global straight_kp
	global straight_ki
	global straight_kd

	if direction =='':
		direction = PERIPH["wheels"].gyro.angle

	# degrees_to_travel = m.degrees(2 * m.pi * wheel_trackdist / wheel_circumference)
	turn_right()
	PERIPH["wheels"].follow_gyro_angle(straight_kp,straight_ki,straight_kd, 15, direction+90, 0.05, follow_for_ms, ms=1000)
	#PERIPH["wheels"].on_for_degrees(left_speed=15,right_speed=15,  degrees=degrees_to_travel)
	turn_right()
	return

def halfturn_left(direction=''):
	"""
	makes a U turn clockwise
	"""
	global PERIPH
	global straight_kp
	global straight_ki
	global straight_kd

	if direction =='':
		direction = PERIPH["wheels"].gyro.angle

	# degrees_to_travel = m.degrees(2 * m.pi * wheel_trackdist / wheel_circumference)
	turn_left()
	PERIPH["wheels"].follow_gyro_angle(straight_kp,straight_ki,straight_kd, 15, direction-90, 0.05, follow_for_ms, ms=1000)
	#PERIPH["wheels"].on_for_degrees(left_speed=15,right_speed=15,  degrees=degrees_to_travel)
	turn_left()
	return

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


def lawnmower():
	global order
	global order_ack
	global stop_pattern
	global end
	old_state = ''
	direction = 0

	while end == False:
		stop()
		while stop_pattern == False:
			if old_state == order:
				continue

			elif order =='straight':
				old_state = order
				stop()
				straight()
				order_ack = False

			elif order =='u-turn right':
				old_state = order
				stop()
				halfturn_right(direction)
				direction+=180
				straight(use_gyro = True, follow_angle = direction) # adjusts turn
				order_ack = True

			elif order =='u-turn left':
				old_state = order
				stop()
				halfturn_left(direction)
				direction-=180
				straight(use_gyro = True, follow_angle = direction) # adjusts turn
				order_ack = True


			
	stop()
	return


def retracting_square():
	global pos_x
	global pos_y
	global targ_x
	global targ_y

	global order
	global order_ack
	global pattern_done
	global stop_pattern
	global end

	global adj_length
	global A_dist
	global B_dist
	global C_dist
	global D_dist

	old_state = ''
	pattern_done = False
	direction = 0
	wall_side_cursor = 0
	wall_side = ['A','B','C','D']

	while end == False:
		stop()
		while stop_pattern == False:
			if old_state == order:
				continue

			elif order =='straight':
				old_state = 'straight'
				stop()
				straight()
				order_ack = False

			elif order =='turn right':

				old_state = 'turn right'
					
				direction += 90
				wall_side_cursor+=1
				if (wall_side_cursor == len(wall_side)) :
					wall_side_cursor=0

				stop()
				turn_right()
				straight(use_gyro = True, follow_angle = direction) # adjusts turn
				order_ack = True


			elif order == 'retract':
				old_state == 'retract'
				what_to_travel= adj_length

				while what_to_travel >= adj_length:
					if order=='stop':
						break

					if wall_side[wall_side_cursor] == 'A':
						A_dist -= (2*adj_length)
						C_dist -= (2*adj_length)
						what_to_travel = A_dist
					elif wall_side[wall_side_cursor] == 'B':
						B_dist -= (2*adj_length)
						D_dist -= (2*adj_length)
						what_to_travel = B_dist
					elif wall_side[wall_side_cursor] == 'C':
						A_dist -= (2*adj_length)
						C_dist -= (2*adj_length)
						what_to_travel = C_dist
					elif wall_side[wall_side_cursor] == 'D':
						B_dist -= (2*adj_length)
						D_dist -= (2*adj_length)
						what_to_travel = D_dist
					# print("what to traviel : {}".format(what_to_travel))

					if what_to_travel < adj_length:
						break
					else:
						# print("moving for less than a wall target distance")
						target_pos = PERIPH["wheels"].left_motor.position + what_to_travel
						PERIPH["wheels"].on(15,15)
						while PERIPH["wheels"].left_motor.position < target_pos:
							if order=='stop':
								break
							continue

						if order=='stop':
							break
						direction += 90
						wall_side_cursor+=1
						if (wall_side_cursor == len(wall_side)) :
							wall_side_cursor=0

						stop()
						turn_right()
						straight(use_gyro = True, follow_angle = direction) # adjusts turn

				pattern_done = True	
				stop()
				order_ack=True
	stop()
	return


# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---
if __name__ == '__main__':
	print("Running movement.py")