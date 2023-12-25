'''input
Y
A
B
N
'''

USER_DEBUG = True

def DEBUG(userinput):
    if (USER_DEBUG):
        print("\n\t> " + userinput)
    return



#!/usr/bin/env python3
# ---  ---  ---  ---  ---  --- ---  ---  ---
# file name:    main.py
# author:      TECHNOBOTS
# date:        2023 11 27
# ---  ---  ---
# ---  ---  ---  ---  ---
# file name:         main.py
# description :      main script handling state machine,
#                    flags, user inputs, etc.
#
# author:            Alexandre MENSAH
# created on:        2023 11 27
# last updated:      2023 12 23
# updated by:        Alexandre EANG
# comment :          * Setup event handling
# ---  ---   ---  ---  ---  ---

#______________________________________________________________
#   ____________________  ___   ______  ____  ____  ___________
#  /_  __/ ____/ ____/ / / / | / / __ \/ __ )/ __ \/_  __/ ___/
#   / / / __/ / /   / /_/ /  |/ / / / / __  / / / / / /  \__ \ 
#  / / / /___/ /___/ __  / /|  / /_/ / /_/ / /_/ / / /  ___/ / 
# /_/ /_____/\____/_/ /_/_/ |_/\____/_____/\____/ /_/  /____/  
# ______________________________________________________________
                                                             


# ---  IMPORTS  ---  ---  ---  ---
# built in modules
import threading
import json
from time import sleep

# user module
import graphics as grph
from initialization import *

# lego modules
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
# --- CONSTANTS / CONFIG

# --- VARIABLES
MACHINE_STATE = 'STATE_INIT'
MACHINE_STATE_OLD = 'STATE_INIT'

# --- ERRor flags
ERR ={
    "port_wheels" : False,
    "port_claw" : False,
    "port_gyro" : False,
    "port_color" : False,
    "port_sonar" : False
}
# ---  ---  ---  ---  ---  ---


# ---  FUNCTION DEFINITION  ---
def main():
    """
    Execute this function to start the program.
    """
    print("\nProgram starting ...\n")

    ERR = init_ports()
    
    if (ERR["port_wheels"]):
        print("\n[?] Setup ports for wheeldrive now ?")
        userinput = input(" |  (Y: proceed / N: cancel)\n").upper()
        check = init_checkwheels(userinput)
        if (check == 1):
            return
    if (ERR["port_claw"]):
        print("\n[?] Setup ports for claw now ?")
        userinput = input(" |  (Y: proceed / N: cancel)\n").upper()
        check = init_checkclaw(userinput)
        if (check == 1):
            return


    # try:
    #     while (True):
    #         pass
    #         # event = eventlisten_statemachine()
    #         # eventlisten_flags()

    #         # if (event == 'None'):
    #         #     pass
    # except:
    #     print("error")
    #     pass
    return



# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---  ---
init()
grph.CLEAR_CONSOLE()
grph.TECHNOBOTS_LOGO()

main()

grph.CLEAR_CONSOLE(15)
grph.TECHNOBOTS_LOGO('left slant')
# ---  ---  ---  ---  ---