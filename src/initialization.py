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
SYS= {
    "port_lwheel" : None,             
    "port_rwheel" : None,             
    "port_claw" : None,               
    "phys_trackdist" : None,          
    "phys_wheeldiameter" : None,      
    "targ_diameter" : None,           
    "targ_color" : None,              
    "envi_width" : None,              
    "envi_length" : None,             
    "envi_floorcolor" : None,         
    "envi_edgecolor" : None,
    "logic_kp": None,
    "logic_ki": None,
    "logic_kd": None,
    "gui_drawrobot": None,   
}


PERIPH = {
    "wheels" : None,
    "claw" : None,
    "gyro" : None,
    "color" : None,
    "sonar" : None
}


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

    global SYS

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
                SYS["port_lwheel"]             = cfg_user['port']['lwheel']
                SYS["port_rwheel"]             = cfg_user['port']['rwheel']
                SYS["port_claw"]               = cfg_user['port']['claw']
                SYS["phys_trackdist"]          = cfg_user['physical']['trackdist']
                SYS["phys_wheeldiameter"]      = cfg_user['physical']['wheeldiameter']
                SYS["targ_diameter"]           = cfg_user['target']['diameter']
                SYS["targ_color"]              = cfg_user['target']['color']
                SYS["envi_width"]              = cfg_user['environment']['width']
                SYS["envi_length"]             = cfg_user['environment']['length']
                SYS["envi_floorcolor"]         = cfg_user['environment']['floorcolor']
                SYS["envi_edgecolor"]          = cfg_user['environment']['edgecolor']
                SYS["logic_kp"]                = cfg_user["logic"]["logic_kp"]
                SYS["logic_ki"]                = cfg_user["logic"]["logic_ki"]
                SYS["logic_kd"]                = cfg_user["logic"]["logic_kd"]
                SYS["gui_drawrobot"]           = cfg_user["gui"]["gui_drawrobot"]
            cfg_user_json.close()
        elif (config == 'default'):
            SYS["port_lwheel"]             = cfg_def['port']['lwheel']
            SYS["port_rwheel"]             = cfg_def['port']['rwheel']
            SYS["port_claw"]               = cfg_def['port']['claw']
            SYS["phys_trackdist"]          = cfg_def['physical']['trackdist']
            SYS["phys_wheeldiameter"]      = cfg_def['physical']['wheeldiameter']
            SYS["targ_diameter"]           = cfg_def['target']['diameter']
            SYS["targ_color"]              = cfg_def['target']['color']
            SYS["envi_width"]              = cfg_def['environment']['width']
            SYS["envi_length"]             = cfg_def['environment']['length']
            SYS["envi_floorcolor"]         = cfg_def['environment']['floorcolor']
            SYS["envi_edgecolor"]          = cfg_def['environment']['edgecolor']
            SYS["logic_kp"]                = cfg_def["logic"]["logic_kp"]
            SYS["logic_ki"]                = cfg_def["logic"]["logic_ki"]
            SYS["logic_kd"]                = cfg_def["logic"]["logic_kd"]
            SYS["gui_drawrobot"]           = cfg_def["gui"]["gui_drawrobot"]
        elif (config == 'reset'):
            with open('../config/config.user.json', 'w') as cfg_user_json:
                json.dump(cfg_def,cfg_user_json, indent=2)
            SYS["port_lwheel"]             = cfg_def['port']['lwheel']
            SYS["port_rwheel"]             = cfg_def['port']['rwheel']
            SYS["port_claw"]               = cfg_def['port']['claw']
            SYS["phys_trackdist"]          = cfg_def['physical']['trackdist']
            SYS["phys_wheeldiameter"]      = cfg_def['physical']['wheeldiameter']
            SYS["targ_diameter"]           = cfg_def['target']['diameter']
            SYS["targ_color"]              = cfg_def['target']['color']
            SYS["envi_width"]              = cfg_def['environment']['width']
            SYS["envi_length"]             = cfg_def['environment']['length']
            SYS["envi_floorcolor"]         = cfg_def['environment']['floorcolor']
            SYS["envi_edgecolor"]          = cfg_def['environment']['edgecolor']
            SYS["logic_kp"]                = cfg_def["logic"]["logic_kp"]
            SYS["logic_ki"]                = cfg_def["logic"]["logic_ki"]
            SYS["logic_kd"]                = cfg_def["logic"]["logic_kd"]
            SYS["gui_drawrobot"]           = cfg_def["gui"]["gui_drawrobot"]
    
    return SYS
    

# def init_save_config():
#     """
#     saves current configuration into local user config
#     """
#     global SYS
#     try:
#         with open('../config/config.user.json', 'w') as cfg_user_json:
#             cfg_user = json.load(cfg_user_json)
#             cfg_user['port']['lwheel']             = SYS["port_lwheel"]
#             cfg_user['port']['rwheel']             = SYS["port_rwheel"]
#             cfg_user['port']['claw']               = SYS["port_claw"]
#             cfg_user['physical']['trackdist']      = SYS["phys_trackdist"]
#             cfg_user['physical']['wheeldiameter']  = SYS["phys_wheeldiameter"]
#             cfg_user['target']['diameter']         = SYS["targ_diameter"]
#             cfg_user['target']['color']            = SYS["targ_color"]
#             cfg_user['environment']['width']       = SYS["envi_width"]
#             cfg_user['environment']['length']      = SYS["envi_length"]
#             cfg_user['environment']['floorcolor']  = SYS["envi_floorcolor"]
#             cfg_user['environment']['edgecolor']   = SYS["envi_edgecolor"]
#     except:
#         print("Error while trying to save configuration.")
#     else:
#         print("Sucesfully saved current configuration to local user configuration.")
#     return

def init_ports():
    """
    """
    ERR_msg = []

    try:
        PERIPH["wheels"] = MoveTank(SYS["port_lwheel"],SYS["port_rwheel"])
        ERR["port_wheels"] =False
    except Exception as e_msg:
        ERR_msg.append(e_msg)
        ERR["port_wheels"] =True

    try:
        PERIPH["claw"] = MediumMotor(SYS["port_claw"])
        ERR["port_claw"] =False
    except Exception as e_msg:
        ERR_msg.append(e_msg)
        ERR["port_claw"] =True
   
    try:
        PERIPH["gyro"] = GyroSensor()
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
    if (ERR["port_wheels"] or ERR["port_claw"]):
        print("Robot configuration can be found under /config directory.")
        print("For permanent changes, modify robot configuration from the")
        print("upcoming menus or directly from /config directory.\n")

    for msg in ERR_msg:
        print("\t>>> {}".format(msg))

    return ERR, PERIPH


def init_checkwheels(userinput="Y"):
    """
    remediates un-initialized wheels port
    """
    global ERR
    global SYS

    if (userinput == "N" ):
        print("\n\nExiting ...")
        return 1, ERR, SYS

    elif (userinput == "Y" ):
        print("\n[?] Register left motor port : ")
        user_leftmotorport = input(" |  (A/B/C/D)\n").upper()
        print("\n[?] Register right motor port : ")
        user_rightmotorport = input(" |  (A/B/C/D)\n").upper()
        try:
            PERIPH["wheels"] = MoveTank('ev3-ports:out'+user_leftmotorport,'ev3-ports:out'+user_rightmotorport)
        except Exception as error:
            print("\n\nAssignement of ports for wheeldrive was unsuccesful.")
            print("\n\t>>> {}\n".format(error))
            print("\n[?] Would you like to select different ports ?")
            checkinput = input(" |  (Y: proceed / N: cancel)\n").upper()
            check = init_checkwheels(checkinput)
            return check
        else:
            SYS["port_lwheel"] = user_leftmotorport
            SYS["port_rwheel"] = user_rightmotorport
            print("Assignement of ports for wheeldrive succesful.")
            ERR["port_wheels"]=False
            return 0, ERR, SYS
        return

    print("\n\t>>> Incorrect argument.")
    print("[?] Setup ports for wheeldrive now ?")
    checkinput = input(" |  (Y: proceed / N: cancel)\n").upper()
    check = init_checkwheels(checkinput)
    return check, ERR, SYS
    
    
def init_checkclaw(userinput="Y"):
    """
    remediates un-initialized claw port
    """
    global ERR
    global SYS

    if (userinput == "N"):
        print("\n\nExiting ...")
        return 1, ERR, SYS

    elif (userinput == "Y"):
        print("[?] Register claw port :")
        user_clawport = input("\n |  (A/B/C/D)\n").upper()

        try:
            PERIPH["claw"] = MediumMotor('ev3-ports:out'+user_clawport)
        except Exception as error:
            print("\n\nAssignement of port for claw was unsuccesful.\n\n")
            print("\n\t>>> {}\n".format(error))
            print("\n[?] Would you like to select a different port ?")
            checkinput = input(" |  (Y: proceed / N: cancel)\n").upper()
            check = init_checkclaw(checkinput)
            return check
        else:
            SYS["port_claw"] = user_clawport
            print("Assignement of port for claw succesful.")
            ERR["port_claw"] = False
            return 0, ERR, SYS
        return

    else:
        print("\n\t>>> Incorrect argument.")
        print("[?] Setup port for claw now ?")
        checkinput = input(" |  (Y: proceed / N: cancel)\n").upper()
        check = init_checkclaw(checkinput)
        return check, ERR, SYS
    return

def init_checksensors(userinput="Y"):
    """
    allows the user to reconnect the sensor of interest
    """
    global ERR
    ERR_msg = []
    if (userinput == "N"):
        print("\n\nExiting ...")
        return 1, ERR

    elif (userinput == "Y"):
        try:
            PERIPH["gyro"] = GyroSensor()
            PERIPH["wheels"].gyro = PERIPH["gyro"]
        except Exception as e_msg:
            ERR_msg.append(e_msg)
            ERR["port_gyro"] = True
        else:
            if ERR["port_gyro"] :
                print("Connection to GyroSensor succesful.")
                ERR["port_gyro"] = False

        try:
            PERIPH["color"] = ColorSensor()
        except Exception as e_msg:
            ERR_msg.append(e_msg)
            ERR["port_color"] =True
        else:
            if ERR["port_color"] :
                print("Connection to ColorSensor succesful.")
                ERR["port_color"] =False

        try:
            PERIPH["sonar"] = UltrasonicSensor()
        except Exception as e_msg:
            ERR_msg.append(e_msg)
            ERR["port_sonar"] =True
        else:
            if ERR["port_sonar"] :
                print("Connection to UltrasonicSensor succesful.")
                ERR["port_sonar"] =False
    
    else:
        print("\n\t>>> Incorrect argument.")
        print("[?] Try reconnecting sensors now ?")
        checkinput = input(" |  (Y: proceed / N: cancel)\n").upper()
        check = init_checksensors(checkinput, sensor)
        return check, ERR

    if (ERR["port_gyro"] or ERR["port_color"] or ERR["port_sonar"]):
        print("\nConfiguration error.")
        print("Check physical connections on robot according to current configuration.")

    for msg in ERR_msg:
        print("\t>>> {}".format(msg))

    return 0, ERR




# ---  ---  ---  ---  ---  ---  ---




# ---  CODE START  ---
# no op
# ---  ---  ---  ---  ---  ---