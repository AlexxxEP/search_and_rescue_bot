'''input
Y
OUTPUT_A
OUTPUT_D
Y
OUTPUT_A
OUTPUT_D
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
# author:      
# date:        2023 11 27
# ---  ---  ---
# ---  ---  ---  ---  ---
# file name:         % name of file + extension %
# description :
#
#
#
# author:            Alexandre MENSAH
# created on:        2023 11 27
# last updated:      2023 11 29
# updated by:        Alexandre EANG
# comment :          * Applied template to this document
# ---  ---   ---  ---  ---  ---



# ---  IMPORTS  ---  ---  ---  ---
import threading
import json

from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from time import sleep
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
# --- CONSTANTS
# list constants declarations here
# --- VARIABLES
# list variable declarations here
# ---  ---  ---  ---  ---  ---



# ---  FUNCTION DEFINITION  ---
def main():
    """
    Execute this function to start the program.
    """

    # Program start
    print("\nStarting program now ...\n")


    # Checking port attribution
    try:
        wheels
        wheels_port_error =False
    except:
        print("\t>>> Ports for wheeldrive have not been defined.")
        wheels_port_error =True
    try:
        claw
        claw_port_error =False
    except:
        print("\t>>> Port for claw has not been defined.")
        claw_port_error =True


    # Fix port attribution
    if (wheels_port_error or claw_port_error):
        print("\nCheck connection on robot according to current configuration.")
        print("Robot configuration can be found under /config directory.")
        print("For permanent changes, use init_config() to modify robot configuration.")

    if (wheels_port_error):
        userinput = input("\nSetup ports for wheeldrive now ? (Y: proceed / N: cancel)")
        check = init_checkwheels(userinput)
        if (check == 1):
            return

    if (claw_port_error):
        userinput = input("\nSetup port for claw now ? (Y: proceed / N: cancel)")
        check = init_checkclaw(userinput)
        if (check == 1):
            return

    claw_open()
    wheels.on(50,50)
    return


def init(left_wheel_port, right_wheel_port, claw_port):
    """
    Initializes the ports of all actuators
    left_wheel_port : output port of the corresponding actuator
    right_wheel_port : output port of the corresponding actuator
    claw_port : output port of the corresponding actuator
    """
    wheels = MoveTank(left_wheel_port, right_wheel_port)
    claw = MediumMotor(claw_port)
    return
    
    
def init_checkwheels(userinput="Y"):
    """
    remediates un-initialized wheels port
    """
    DEBUG(userinput)

    if (userinput == "N" or userinput == "n"):
        print("\n\nExiting ...")
        return 1

    elif ( userinput == "Y" or userinput == "y"):
        user_leftmotorport = input("\nRegister left motor port :\n")
        DEBUG(user_leftmotorport)
        user_rightmotorport = input("\nRegister right motor port :\n")
        DEBUG(user_rightmotorport)
        try:
            wheels = MoveTank(user_leftmotorport,user_rightmotorport)
        except Exception as error:
            print("\nAssignement of ports for wheeldrive was unsuccesful.\n\n")
            print("\t>>> ",error)
            checkinput = input("\n\nWould you like to select different ports ? (Y/N)")
            check = init_checkwheels(checkinput)
            return check
        else:
            Print("Assignement of ports for wheeldrive succesful.")
            return 0
        return

    else:
        print("\nIncorrect argument.")
        checkinput = input("Setup ports for wheeldrive now ? (Y: proceed / N: cancel)\n")
        check = init_checkwheels(checkinput)
        return check
    return
    
    
def init_checkclaw(userinput):
    """
    remediates un-initialized claw port
    """
    if(USER_DEBUG):
        print("\n\t> " + userinput) # just for seeing inputs in console (Alexandre EANG)


    if (userinput == "N" or userinput == "n"):
        print("\n\nExiting ...")
        return 1

    elif ( userinput == "Y" or userinput == "y"):
        user_clawport = input("\nRegister claw motor port :\n")
        DEBUG(claw_port)

        try:
            claw = MediumMotor(user_clawport)
        except Exception as error:
            print("\nAssignement of port for claw was unsuccesful.\n\n")
            print("\t>>> ",error)
            checkinput = input("\n\nWould you like to select a different port ? (Y/N)")
            check = init_checkclaw(checkinput)
            return check
        else:
            Print("Assignement of port for claw succesful.")
            return 0
        return

    else:
        print("\nIncorrect argument.")
        checkinput = input("Setup port for claw now ? (Y: proceed / N: cancel)\n")
        DEBUG(checkinput)
        check = init_checkclaw(checkinput)
        return check
    return
# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---  ---
main()
# with open('../config/config.default.json','r') as cfg:
#     prout = json.load(cfg)["ports"]

# with open('../config/config.user.json','r') as cfg:
#     caca = json.load(cfg)["ports"]


# try:
#     lwheelport = prout["left_wheel"]
#     lwheelport = caca["left_wheel"]
# except:
#     pass
# try:
#     rwheelport = prout["right_wheel"]
#     rwheelport = caca["right_wheel"]
# except:
#     pass

# print(lwheelport)
# print(rwheelport)
# ---  ---  ---  ---  ---