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
# last updated:      2024 01 09
# updated by:        Alexandre EANG
# comment :          * Integrated movement patterns
# ---  ---   ---  ---  ---  ---



#______________________________________________________________
#   ____________________  ___   ______  ____  ____  ___________
#  /_  __/ ____/ ____/ / / / | / / __ \/ __ )/ __ \/_  __/ ___/
#   / / / __/ / /   / /_/ /  |/ / / / / __  / / / / / /  \__ \ 
#  / / / /___/ /___/ __  / /|  / /_/ / /_/ / /_/ / / /  ___/ / 
# /_/ /_____/\____/_/ /_/_/ |_/\____/_____/\____/ /_/  /____/  
# ______________________________________________________________
#


# ---  IMPORTS  ---  ---  ---  ---
# built in modules
print("# importing io")
import io
print("# importing threading")
import threading
print("# importing json")
import json
print("# importing sleep from time")
from time import sleep

# user module
import graphics as grph
import menu
from initialization import *
import movement as mv

# ev3dev2 modules
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *

print("# Done importing")
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
# --- CONSTANTS / CONFIG
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SYS= {
    "SYS_port_lwheel" : "",             
    "SYS_port_rwheel" : "",             
    "SYS_port_claw" : "",               
    "SYS_phys_trackdist" : "",          
    "SYS_phys_wheeldiameter" : "",      
    "SYS_targ_diameter" : "",           
    "SYS_targ_color" : "",              
    "SYS_envi_width" : "",              
    "SYS_envi_length" : "",             
    "SYS_envi_floorcolor" : "",         
    "SYS_envi_edgecolor" : ""           
}





# --- VARIABLES
MACHINE_STATE = 'STATE_INIT'
MACHINE_STATE_OLD = 'STATE_INIT'



# --- PERIPHERALS
PERIPH = {
    "wheels" : None,
    "claw" : None,
    "gyro" : None,
    "color" : None,
    "sonar" : None
}

# --- ERRor flags
ERR ={
    "port_wheels" : False,
    "port_claw" : False,
    "port_gyro" : False,
    "port_color" : False,
    "port_sonar" : False
}
# ---  ---  ---  ---  ---  ---



# ---  MAIN DEFINITION  ---

def main():
    print("\nProgram starting ...\n")


    # ----------------------- HARDWARE INIT --------------------
    ERR,PERIPH = init_ports()

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
    for obj in ERR:
        if ERR[obj]:
            print("\n[?] Reconnect ports for sensors now ?")
            userinput = input(" |  (Y: proceed / N: cancel)\n").upper()
            check = init_checksensor(userinput, obj)
            if (check == 1):
                return
    mv.init(PERIPH)


    # ------------------------ CALIBRATION -------------------
    T_loading = threading.Thread(
        target=grph.loading_animation,
        args=('Calibrating gyro, do not move', 30 ,6400))
    T_loading.start()
    PERIPH["gyro"].calibrate()
    grph.loading_flag = False
    T_loading.join()

    T_loading = threading.Thread(
        target=grph.loading_animation,
        args=('Calibrating color sensor, do not move', 30 ,3600))
    T_loading.start()
    PERIPH["color"].calibrate_white()
    grph.loading_flag = False
    T_loading.join()



    grph.CLEAR_CONSOLE()
    grph.TECHNOBOTS_LOGO()

    menu.help()
    # ----------------------------------- USER INTERACTION STARTS --------------------------------
    while True:
        user_cmd = input()
        print("\n")


        # START MENU SUB-ROUTINE
        if (user_cmd.lower() == 'start'):

            menu.action = 'None'
            menu.action_ack = False
            grph.activate = False
            grph.end = False
            grph.stopack = False

            T_menu = threading.Thread(target = menu.start)
            T_menu.start()
            T_graphic = threading.Thread(
                target = grph.blinker,
                args = (PERIPH["wheels"],PERIPH["claw"])
                )
            T_graphic.start()

            while (menu.action == 'None'):
                continue
            if (menu.action=='run to line'):
                grph.activate = True
                mv.straight(8)
            while (PERIPH["color"].color != 1):
                continue
            mv.straight(3)
            while (PERIPH["color"].color == 1):
                continue
            mv.stop()
            grph.activate = False
            while(grph.stopack != True):
                continue

            menu.action_ack = True
            grph.end = True

            T_menu.join()
            T_graphic.join()

            mv.retracting_circle()

            print("all processes done")


        # CALIBRATION MENU SUB-ROUTINE
        elif (user_cmd.lower() == 'calibrate'):
            T_graphic = threading.Thread(
                target=grph.loading_animation,
                args=('Calibrating gyro, do not move', 30 ,6400)
                )
            T_graphic.start()
            PERIPH["wheels"].gyro.calibrate()
            grph.loading_flag = False
            T_graphic.join()

            T_graphic = threading.Thread(
                target=grph.loading_animation,
                args=('Calibrating color sensor, do not move', 30 ,3600)
                )
            T_graphic.start()
            PERIPH["color"].calibrate_white()
            grph.loading_flag = False
            T_graphic.join()
            continue


        # CONFIGURATION MENU SUB-ROUTINE
        elif (user_cmd.lower() == 'config'):
            print('not yet implemented')
            continue


        # SPIN COMMAND SUB-ROUTINE
        elif (user_cmd.lower() == 'spin'):
            PERIPH["wheels"].on(-8,8)
            continue


        # STOP COMMAND SUB-ROUTINE
        elif (user_cmd.lower() == 'stop'):
            PERIPH["wheels"].on(0,0)
            continue
        

        # HELP MENU
        elif (user_cmd.lower() == 'help'):
            menu.help()
            continue


        # EXIT COMMAND
        elif (user_cmd.lower() == 'exit'):
            return



        # ETC COMMANDS
        elif (user_cmd.lower() == ''):
            continue
        else:
            print("Invalid argument.")
            print("\n\t>>> {} is not recognized as a command.\n".format(user_cmd.lower()))


    return


# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---  ---
init()
print(SYS_port_claw)
main()

# grph.CLEAR_CONSOLE()
grph.TECHNOBOTS_LOGO('left slant')
# grph.ROBOT()

# ---  ---  ---  ---  ---