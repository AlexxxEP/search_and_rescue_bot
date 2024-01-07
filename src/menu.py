#!/usr/bin/env python3
# ---  ---  ---  ---  ---
# file name:         menu.py
# description :		 handles the console menus
#
# author:            Alexandre EANG
# created on:        2023 12 26
# last updated:      2023 12 26
# updated by:        Alexandre EANG
# comment :          * Created file
# ---  ---   ---  ---  ---  ---
if (__name__ != '__main__'): print("# importing {}".format(__name__))



# ---  IMPORTS  ---  ---  ---  ---
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
# --- CONSTANTS / CONFIG
# --- GRAPHIC RESSOURCES  
# ---  ---  ---  ---  ---  ---



# ---  FUNCTION DEFINITION  ---
def help():
	print("\n")
	print("[?] Type in a command to start")
	print(" |  start :     opens start menu")
	print(" |  calibrate : opens calibration menu")
	print(" |  config :    loads")
	print(" |  spin :      spins the robot")
	print(" |  stop :      stop robot actuators")
	print(" |  help :      displays this message")
	print(" |                                   ")
	print(" |  exit :      exits program")
	return


def start():
	global action
	global action_ack
	print("\n")
	print("[?] Place the robot about 10cm behind the starting line.")
	print(" |  Type in any key when ready.")
	print(" | ")
	print(" |  To abort, do CMD+C.")
	try:
		input()
	except KeyboardInterrupt:
		return

	action='run to line'
	while action_ack != True:
		continue

	print("\n")
	print("[?] Select a pattern to start the robot.")
	print(" |  1 :     Snake patter/lawnmower")
	print(" |                                   ")
	print(" |  To abort, do CMD+C.")
	try:
		input()
	except KeyboardInterrupt:
		return
	return



# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---
if __name__ == '__main__':
	print("testing")