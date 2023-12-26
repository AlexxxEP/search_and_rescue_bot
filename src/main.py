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

# ev3dev2 modules
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *

print("# Done importing")
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
# --- CONSTANTS / CONFIG
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# --- VARIABLES
MACHINE_STATE = 'STATE_INIT'
MACHINE_STATE_OLD = 'STATE_INIT'



# --- PERIHPERALS
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



# ---  FUNCTION DEFINITION  ---
def main():

    print("\nProgram starting ...\n")

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


    T_temp = threading.Thread(
        target=grph.loading_animation,
        args=('Calibrating gyro, do not move', 30 ,6400))
    T_temp.start()
    PERIPH["wheels"].gyro.calibrate()
    grph.loading_flag = False
    T_temp.join()


    T_temp = threading.Thread(
        target=grph.loading_animation,
        args=('Calibrating color sensor, do not move', 30 ,3600))
    T_temp.start()
    PERIPH["color"].calibrate_white()
    grph.loading_flag = False
    T_temp.join()

    grph.CLEAR_CONSOLE()
    grph.TECHNOBOTS_LOGO()


    menu.help()
    # ----------------------------------- USER INTERACTION STARTS --------------------------------
    while True:
        user_cmd = input()
        print("\n")


        if (user_cmd.lower() == 'start'):
            menu.action = 'None'
            menu.action_ack = False
            grph.activate = False
            grph.end = False
            grph.stopack = False

            T0 = threading.Thread(target = menu.start)
            T0.start()
            T1 = threading.Thread(target = grph.blinker, args = (PERIPH["wheels"],PERIPH["claw"]))
            T1.start()

            while (menu.action == 'None'):
                continue
            if (menu.action=='run to line'):
                grph.activate = True
                PERIPH["wheels"].on(8,8)
            while (PERIPH["color"].color != 1):
                continue
            PERIPH["wheels"].on(3,3)
            while (PERIPH["color"].color == 1):
                continue
            PERIPH["wheels"].on(0,0)
            grph.activate = False
            while(grph.stopack != True):
                continue

            menu.action_ack = True
            grph.end = True

            T0.join()
            T1.join()
            print("all processes done")

        elif (user_cmd.lower() == 'calibrate'):
            T_temp = threading.Thread(
                target=grph.loading_animation,
                args=('Calibrating gyro, do not move', 30 ,6400))
            T_temp.start()
            PERIPH["wheels"].gyro.calibrate()
            grph.loading_flag = False
            T_temp.join()

            T_temp = threading.Thread(
                target=grph.loading_animation,
                args=('Calibrating color sensor, do not move', 30 ,3600))
            T_temp.start()
            PERIPH["color"].calibrate_white()
            grph.loading_flag = False
            T_temp.join()
            continue
        elif (user_cmd.lower() == 'config'):
            print('not yet implemented')
            continue
        elif (user_cmd.lower() == 'spin'):
            PERIPH["wheels"].on(-8,8)
            continue
        elif (user_cmd.lower() == 'stop'):
            PERIPH["wheels"].on(0,0)
            continue
        elif (user_cmd.lower() == 'help'):
            menu.help()
            continue
        elif (user_cmd.lower() == 'exit'):
            return

        elif (user_cmd.lower() == ''):
            continue
        else:
            print("Invalid argument.")
            print("\n\t>>> '{}' is not recognized as a command.\n".format(user_cmd.lower()))




    #     while (True):
    #         pass
    #         # event = eventlisten_statemachine()
    #         # eventlisten_flags()

    #         # if (event == 'None'):
    #         #     pass
    # except KeyboardInterrupt:
    #     print("User terminated main().")
    #     print("Exiting ...")
    #     pass
    return


# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---  ---
init()
main()

# grph.CLEAR_CONSOLE()
grph.TECHNOBOTS_LOGO('left slant')
# grph.ROBOT()

# ---  ---  ---  ---  ---