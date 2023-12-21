'''input
N
'''

USER_DEBUG = False

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
# last updated:      2023 12 20
# updated by:        Alexandre EANG
# comment :          * Setup event handling
# ---  ---   ---  ---  ---  ---



# ---  IMPORTS  ---  ---  ---  ---
import threading
import json

from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from time import sleep
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
# --- CONSTANTS / CONFIG

# --- VARIABLES
MACHINE_STATE = 'STATE_INIT'
MACHINE_STATE_OLD = 'STATE_INIT'
ERR_port_claw = False
ERR_port_wheels = False
# ---  ---  ---  ---  ---  ---



# ---  FUNCTION DEFINITION  ---
def main():
    """
    Execute this function to start the program.
    """
    print("\nProgram starting ...\n")

    init_ports()
    
    if (ERR_port_wheels or ERR_port_claw):
        print("\nCheck connection on robot according to current configuration.")
        print("Robot configuration can be found under /config directory.")
        print("For permanent changes, use init_configure() to modify robot configuration.")
    if (ERR_port_wheels):
        userinput = input("\nSetup ports for wheeldrive now ? (Y: proceed / N: cancel)\n").upper()
        check = init_checkwheels(userinput)
        if (check == 1):
            return
    if (ERR_port_claw):
        userinput = input("\nSetup port for claw now ? (Y: proceed / N: cancel)\n").upper()
        check = init_checkclaw(userinput)
        if (check == 1):
            return


    # while (True):
    #     event = eventlisten_statemachine()
    #     eventlisten_flags()

    #     if (event == 'None'):
    #         pass

    return


def init(config='user'):
    """
    Initializes the software settings by importing config file.
    By default, the config file used is the user config.
    If the user wants to apply the default configuration, 
    user may pass 'default' as argument.

    Argument 'config':
    - 'user'    :   initializes software with user config.
                    when parameter can't be found, default
                    configuration parameters will be used.

    - 'default' :   initializes software with default config
                    without updating user config.

    - 'reset'   :   overwrite user config with default config,
                    then intializes software with user config.
    """
    if (config != 'user' and config != 'default' and config != 'reset'):
        print("\n\t>>> Wrong argument.")
        return 1

    global SYS_port_lwheel      
    global SYS_port_rwheel      
    global SYS_port_claw        
    global SYS_phys_trackdist   
    global SYS_phys_wheeldiameter
    global SYS_targ_diameter    
    global SYS_targ_color       
    global SYS_envi_width       
    global SYS_envi_length      
    global SYS_envi_floorcolor  
    global SYS_envi_edgecolor   

    try:
        cfg_user_json = open('../config/config.user.json', 'r')
        cfg_user = json.load(cfg_user_json)
    except:
        cfg_user_json = open('../config/config.user.json','w')
        config = 'reset'
    finally:
        cfg_user_json.close()


    with open('../config/config.default.json', 'r') as cfg_def_json:
        cfg_def = json.load(cfg_def_json)     
        if (config == 'user'):
            with open('../config/config.user.json', 'r') as cfg_user_json:
                cfg_user = json.load(cfg_user_json)
                SYS_port_lwheel             = cfg_user['port']['lwheel']
                SYS_port_rwheel             = cfg_user['port']['rwheel']
                SYS_port_claw               = cfg_user['port']['claw']
                SYS_phys_trackdist          = cfg_user['physical']['trackdist']
                SYS_phys_wheeldiameter      = cfg_user['physical']['wheeldiameter']
                SYS_targ_diameter           = cfg_user['target']['diameter']
                SYS_targ_color              = cfg_user['target']['color']
                SYS_envi_width              = cfg_user['environment']['width']
                SYS_envi_length             = cfg_user['environment']['length']
                SYS_envi_floorcolor         = cfg_user['environment']['floorcolor']
                SYS_envi_edgecolor          = cfg_user['environment']['edgecolor']
            cfg_user_json.close()
        elif (config == 'default'):
            SYS_port_lwheel             = cfg_def['port']['lwheel']
            SYS_port_rwheel             = cfg_def['port']['rwheel']
            SYS_port_claw               = cfg_def['port']['claw']
            SYS_phys_trackdist          = cfg_def['physical']['trackdist']
            SYS_phys_wheeldiameter      = cfg_def['physical']['wheeldiameter']
            SYS_targ_diameter           = cfg_def['target']['diameter']
            SYS_targ_color              = cfg_def['target']['color']
            SYS_envi_width              = cfg_def['environment']['width']
            SYS_envi_length             = cfg_def['environment']['length']
            SYS_envi_floorcolor         = cfg_def['environment']['floorcolor']
            SYS_envi_edgecolor          = cfg_def['environment']['edgecolor']
        elif (config == 'reset'):
            with open('../config/config.user.json', 'w') as cfg_user_json:
                json.dump(cfg_def,cfg_user_json, indent=2)
            SYS_port_lwheel             = cfg_def['port']['lwheel']
            SYS_port_rwheel             = cfg_def['port']['rwheel']
            SYS_port_claw               = cfg_def['port']['claw']
            SYS_phys_trackdist          = cfg_def['physical']['trackdist']
            SYS_phys_wheeldiameter      = cfg_def['physical']['wheeldiameter']
            SYS_targ_diameter           = cfg_def['target']['diameter']
            SYS_targ_color              = cfg_def['target']['color']
            SYS_envi_width              = cfg_def['environment']['width']
            SYS_envi_length             = cfg_def['environment']['length']
            SYS_envi_floorcolor         = cfg_def['environment']['floorcolor']
            SYS_envi_edgecolor          = cfg_def['environment']['edgecolor']
    return
    

def init_ports():
    """
    """
    global ERR_port_wheels
    global ERR_port_claw
    try:
        wheels = MoveTank(SYS_port_lwheel,SYS_port_rwheel)
        ERR_port_wheels =False
    except:
        print("\t>>> Ports for wheeldrive have not been defined.")
        ERR_port_wheels =True
    try:
        claw = MediumMotor(SYS_port_claw)
        ERR_port_claw =False
    except:
        print("\t>>> Port for claw has not been defined.")
        ERR_port_claw =True
    return



def init_checkwheels(userinput="Y"):
    """
    remediates un-initialized wheels port
    """
    DEBUG(userinput)

    if (userinput == "N" ):
        print("\n\nExiting ...")
        return 1

    elif (userinput == "Y" ):
        user_leftmotorport = input("\nRegister left motor port : (A/B/C/D)\n").upper()
        DEBUG(user_leftmotorport)
        user_rightmotorport = input("\nRegister right motor port : (A/B/C/D)\n").upper()
        DEBUG(user_rightmotorport)
        try:
            wheels = MoveTank('ev3-ports:out'+user_leftmotorport,'ev3-ports:out'+user_rightmotorport)
        except Exception as error:
            print("\nAssignement of ports for wheeldrive was unsuccesful.\n\n")
            print("\t>>> ",error)
            checkinput = input("\n\nWould you like to select different ports ? (Y/N)\n").upper()
            check = init_checkwheels(checkinput)
            return check
        else:
            print("Assignement of ports for wheeldrive succesful.")
            return 0
        return

    print("\nIncorrect argument.")
    checkinput = input("Setup ports for wheeldrive now ? (Y: proceed / N: cancel)\n").upper()
    check = init_checkwheels(checkinput)
    return check
    
    
def init_checkclaw(userinput):
    """
    remediates un-initialized claw port
    """
    if(USER_DEBUG):
        print("\n\t> " + userinput) # just for seeing inputs in console (Alexandre EANG)


    if (userinput == "N"):
        print("\n\nExiting ...")
        return 1

    elif (userinput == "Y"):
        user_clawport = input("\nRegister claw motor port : (A/B/C/D)\n").upper()
        DEBUG(user_clawport)

        try:
            claw = MediumMotor('ev3-ports:out'+user_clawport)
        except Exception as error:
            print("\nAssignement of port for claw was unsuccesful.\n\n")
            print("\t>>> ",error)
            checkinput = input("\n\nWould you like to select a different port ? (Y/N)\n").upper()
            check = init_checkclaw(checkinput)
            return check
        else:
            print("Assignement of port for claw succesful.")
            return 0
        return

    else:
        print("\nIncorrect argument.")
        checkinput = input("Setup port for claw now ? (Y: proceed / N: cancel)\n").upper()
        DEBUG(checkinput)
        check = init_checkclaw(checkinput)
        return check
    return
# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---  ---
init()

main()
# ---  ---  ---  ---  ---