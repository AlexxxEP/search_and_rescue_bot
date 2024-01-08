#!/usr/bin/env python3
# ---  ---  ---  ---  ---
# file name:         initialization.py
# description :		 init sequence functions
#
# author:            Alexandre EANG
# created on:        2023 12 24
# last updated:      2023 12 24
# updated by:        Alexandre EANG
# comment :          * Created file
# 				 	 * Moved existing functions
#					   from main to here
# ---  ---   ---  ---  ---  ---




# ---  IMPORTS  ---  ---  ---  ---
print("# importing {}".format(__name__))
# python modules
import json

# lego modules
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
PERIPH = {
    "wheels" : None,
    "claw" : None,
    "gyro" : None,
    "color" : None,
    "sonar" : None
}

# SYS_port_lwheel
# SYS_port_rwheel
# SYS_port_claw
# SYS_phys_trackdist
# SYS_phys_wheeldiameter
# SYS_targ_diameter
# SYS_targ_color
# SYS_envi_width
# SYS_envi_length
# SYS_envi_floorcolor
# SYS_envi_edgecolor

ERR = {
    "port_wheels" : False,
    "port_claw" : False,
    "port_gyro" : False,
    "port_color" : False,
    "port_sonar" : False
    }
# ---  ---  ---  ---  ---  ---



# ---  FUNCTION DEFINITION  ---
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
    ERR_msg = []

    try:
        PERIPH["wheels"] = MoveTank(SYS_port_lwheel,SYS_port_rwheel)
        ERR["port_wheels"] =False
    except Exception as e_msg:
        ERR_msg.append(e_msg)
        ERR["port_wheels"] =True

    try:
        PERIPH["claw"] = MediumMotor(SYS_port_claw)
        ERR["port_claw"] =False
    except Exception as e_msg:
        ERR_msg.append(e_msg)
        ERR["port_claw"] =True
   
    try:
        PERIPH["wheels"].gyro = GyroSensor()
        ERR["port_gyro"] =False
    except Exception as e_msg:
        ERR_msg.append(e_msg)
        ERR["port_gyro"] =True
  
    try:
        PERIPH["color"] = ColorSensor()
        ERR["port_color"] =False
    except Exception as e_msg:
        ERR_msg.append(e_msg)
        ERR["port_color"] =True
  
    try:
        PERIPH["sonar"] = UltrasonicSensor()
        ERR["port_sonar"] =False
    except Exception as e_msg:
        ERR_msg.append(e_msg)
        ERR["port_sonar"] =True

    if ( ERR["port_wheels"] == False and ERR["port_gyro"] == False ):
        PERIPH["wheels"].gyro = PERIPH["gyro"]


    if (ERR["port_wheels"] or ERR["port_claw"] or ERR["port_gyro"] or ERR["port_color"] or ERR["port_sonar"]):
        print("\nConfiguration error.")
        print("Check physical connections on robot according to current configuration.")
        print("Robot configuration can be found under /config directory.")
        print("For permanent changes, use init_configure() to modify robot configuration.\n")

    for msg in ERR_msg:
        print("\t>>> {}".format(msg))

    return ERR, PERIPH


def init_checkwheels(userinput="Y"):
    """
    remediates un-initialized wheels port
    """

    if (userinput == "N" ):
        print("\n\nExiting ...")
        return 1

    elif (userinput == "Y" ):
        print("\n[?] Register left motor port : ")
        user_leftmotorport = input(" |  (A/B/C/D)\n").upper()
        print("\n[?] Register left motor port : ")
        user_rightmotorport = input(" |  (A/B/C/D)\n").upper()
        try:
            wheels = MoveTank('ev3-ports:out'+user_leftmotorport,'ev3-ports:out'+user_rightmotorport)
        except Exception as error:
            print("\n\nAssignement of ports for wheeldrive was unsuccesful.")
            print("\n\t>>> {}\n".format(error))
            print("\n[?] Would you like to select different ports ?")
            checkinput = input(" |  (Y: proceed / N: cancel)\n").upper()
            check = init_checkwheels(checkinput)
            return check
        else:
            print("Assignement of ports for wheeldrive succesful.")
            return 0
        return

    print("\n\t>>> Incorrect argument.")
    print("[?] Setup ports for wheeldrive now ?")
    checkinput = input(" |  (Y: proceed / N: cancel)\n").upper()
    check = init_checkwheels(checkinput)
    return check
    
    
def init_checkclaw(userinput):
    """
    remediates un-initialized claw port
    """
    if (userinput == "N"):
        print("\n\nExiting ...")
        return 1

    elif (userinput == "Y"):
        print("[?] Register claw port :")
        user_clawport = input("\n |  (A/B/C/D)\n").upper()

        try:
            claw = MediumMotor('ev3-ports:out'+user_clawport)
        except Exception as error:
            print("\n\nAssignement of port for claw was unsuccesful.\n\n")
            print("\n\t>>> {}\n".format(error))
            print("\n[?] Would you like to select a different port ?")
            checkinput = input(" |  (Y: proceed / N: cancel)\n").upper()
            check = init_checkclaw(checkinput)
            return check
        else:
            print("Assignement of port for claw succesful.")
            return 0
        return

    else:
        print("\n\t>>> Incorrect argument.")
        print("[?] Setup port for claw now ?")
        checkinput = input(" |  (Y: proceed / N: cancel)\n").upper()
        check = init_checkclaw(checkinput)
        return check
    return


# ---  ---  ---  ---  ---  ---  ---




# ---  CODE START  ---
# no op
# ---  ---  ---  ---  ---  ---