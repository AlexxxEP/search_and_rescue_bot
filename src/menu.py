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
	print(" |  config :    configuration options")
	print(" |  spin :      spins the robot clockwise")
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
	print(" |  0 :     Back to main menu.")
	try:
		input()
	except KeyboardInterrupt:
		return

	action='run to line'
	while action_ack != True:
		continue
	action_ack = False

	valid_option = False
	while (valid_option != True):
		print("\n")
		print("[?] Select a pattern to start the robot.")
		print(" |  1 :     Snake pattern/lawnmower")
		print(" |  2 :     Retracting squares")
		print(" |  3 :     Camera sweep")
		print(" |                                   ")
		print(" |  0 :     Back to main menu.")
		
		try:
			user_input = input()
		except KeyboardInterrupt:
			return

		if (user_input == '1'):
			action = 'lawnmower'
		elif (user_input == '2'):
			action = 'retracting squares'
		elif (user_input == '3'):
			action = 'camera sweep'
		elif(user_input == '0'):
			action = 'main menu'

		else:
			continue

		valid_option = True
	return


def configure():
	global action

	valid_option = False
	while (valid_option != True):
		print("\n")
		print("[?] Select an option from the list below")
		print(" |  1 :     Apply default configuration")
		print(" |  2 :     Apply local configuration")
		print(" |  3 :     Modify local configuration")
		print(" |  4 :     Reset local configuration")
		print(" |  5 :     Consult configuration")
		print(" |  ")
		print(" |  0 :     Back to main menu.")
		try:
			user_input = input()
		except KeyboardInterrupt:
			return
		
		if (user_input == '1'):
			user_choice = 'default cfg'
		elif (user_input == '2'):
			user_choice = 'user cfg'
		elif (user_input == '3'):
			user_choice = 'modify cfg'
		elif (user_input == '4'):
			user_choice = 'reset cfg'
		elif (user_input == '5'):
			user_choice = 'check cfg'
		elif (user_input == '0'):
			user_choice = 'main menu'
		else:
			print("Invalid argument.")
			print("\n\t>>> {} is not recognized as a command.\n".format(user_input.lower()))
			continue
		valid_option = True

	if user_choice == 'reset cfg':
		print("\n")
		print("[!] Reseting local configuration is a destructive operation !")
		print(" |  The software will then expect the peripherals to be cabled as described")
		print(" |  in the default configuration. If the robot does not function properly ")
		print(" |  after this step, there will be no going back to the local configuration.")
		print("")
		print("[?] Proceed anyway ?")
		checkinput = input(" |  (Y: proceed / N: cancel)\n").upper()
		if checkinput == 'N':
			return 'main menu'
	
	return user_choice

# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---
if __name__ == '__main__':
	print("testing")