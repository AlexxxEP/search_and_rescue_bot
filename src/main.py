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
import sensors as sns

# ev3dev2 modules
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *

print("# Done importing")
# ---  ---   ---  ---  ---  ---



# ---  DECLARATIONS  ---
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# --- CONFIG
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

# --- VARIABLES
MACHINE_STATE = 'STATE_INIT'
MACHINE_STATE_OLD = 'STATE_INIT'
# ---  ---  ---  ---  ---  ---



# ---  MAIN DEFINITION  ---

def main():
    print("\nProgram starting ...\n")


    # ----------------------- HARDWARE INIT --------------------
    global ERR, PERIPH, SYS
    ERR,PERIPH = init_ports()

    if (ERR["port_wheels"]):
        print("\n[?] Setup ports for wheeldrive now ?")
        userinput = input(" |  (Y: proceed / N: cancel)\n").upper()
        check, ERR, SYS = init_checkwheels(userinput)
        if (check == 1):
            return
    if (ERR["port_claw"]):
        print("\n[?] Setup ports for claw now ?")
        userinput = input(" |  (Y: proceed / N: cancel)\n").upper()
        check, ERR, SYS = init_checkclaw(userinput)
        if (check == 1):
            return
    while (ERR["port_gyro"] or ERR["port_color"] or ERR["port_sonar"]):
        print("\n[?] Try reconnecting sensors now ?")
        userinput = input(" |  (Y: proceed / N: cancel)\n").upper()
        check, ERR = init_checksensors(userinput)
        if (check == 1):
            return

    # init_save_config()
    mv.init(PERIPH, SYS)
    sns.init(PERIPH, SYS)
    grph.init(PERIPH, SYS)


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
    # ============    USER INTERACTION STARTS    ====================
    while True:
        user_cmd = input()
        print("\n")


        # START MENU SUB-ROUTINE    ====    ====    ====    ====    
        if (user_cmd.lower() == 'start'):

            # ----    START
            # variables init
            menu.action = 'None'
            menu.action_ack = False
            grph.activate = False
            grph.end = False
            grph.stopack = False    # read only
            
            # threads
            T_menu = threading.Thread(target = menu.start)
            T_menu.start()
            T_graphic = threading.Thread(target = grph.blinker)
            T_graphic.start()

            # runto line
            while (menu.action == 'None'):
                continue
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

            grph.end = True
            menu.action_ack = True
            T_graphic.join()
            T_menu.join()
            while (menu.action == 'run to line'):
                continue

            # ----    PATTERN
            # var init
            grph.activate = False
            grph.end = False
            grph.stopack = False    # read only
            mv.order = ''
            mv.order_ack = False
            mv.stop_pattern = True
            mv.pattern_done = False
            mv.end = False

            mv.pos_x = 0
            mv.pos_y = 0
            mv.targ_x = -1
            mv.targ_y = -1


            if (menu.action == 'lawnmower'):
                mv.A_dist = 0
                mv.B_dist = 0

                grph.end = False
                grph.activate = False
                grph.stopack = False #read only

                PERIPH["gyro"].reset()
                T_pattern = threading.Thread( target = mv.lawnmower)
                T_graphic = threading.Thread(target = grph.blinker)
                T_pattern.start()
                T_graphic.start()

                mv.stop_pattern = False
                grph.activate = True

                # evaluate boundaries
                mv.order='straight'
                mv.A_dist -= PERIPH["wheels"].left_motor.position
                while (PERIPH["color"].color != 1):
                    continue
                mv.A_dist += PERIPH["wheels"].left_motor.position
                mv.order='u-turn right'
                while mv.order_ack != True:
                    continue

                # start loops
                while mv.stop_pattern != True:
                    mv.B_dist = PERIPH["wheels"].left_motor.position
                    mv.order='straight'
                    while (PERIPH["color"].color != 1):
                        if PERIPH["wheels"].left_motor.position > mv.B_dist+mv.A_dist + mv.hairpin_tol:
                            mv.stop_pattern = True
                            break
                    if mv.stop_pattern == True:
                        break                    
                    mv.order='u-turn left'
                    while mv.order_ack != True:
                        continue

                    mv.B_dist = PERIPH["wheels"].left_motor.position
                    mv.order='straight'
                    while (PERIPH["color"].color != 1):
                        if PERIPH["wheels"].left_motor.position > mv.B_dist+mv.A_dist + mv.hairpin_tol:
                            mv.stop_pattern = True
                            break
                    if mv.stop_pattern == True:
                            break
                    mv.order='u-turn right'
                    while mv.order_ack != True:
                        continue



                mv.stop_pattern = True
                mv.end = True
                grph.end = True
                T_pattern.join()                # T_graphic.join()
                T_graphic.join()

            if (menu.action == 'retracting squares'):
                mv.adj_length = 0
                mv.A_dist = 0
                mv.B_dist = 0
                mv.C_dist = 0
                mv.D_dist = 0

                grph.end = False
                grph.activate = False
                grph.stopack = False #read only


                sns.sonar_detected=False
                sns.sonar_enable=True

                PERIPH["gyro"].reset()
                T_pattern = threading.Thread(target = mv.retracting_square)
                T_graphic = threading.Thread(target = grph.blinker)
                T_sensor = threading.Thread(
                    target = sns.poll_sonar,
                    args = (15,150)
                    )
                T_pattern.start()
                T_sensor.start()
                T_graphic.start()

                mv.order = ''
                mv.stop_pattern = False
                grph.activate = True


                # first lap => measures ring
                mv.adj_length-= PERIPH["wheels"].left_motor.position
                mv.straight(use_gyro = True, follow_angle = 0)
                mv.adj_length+= PERIPH["wheels"].left_motor.position
                mv.A_dist  -= PERIPH["wheels"].left_motor.position
                mv.order='straight'
                while (PERIPH["color"].color != 1):
                    continue
                mv.A_dist  += PERIPH["wheels"].left_motor.position
                mv.order='turn right'
                while mv.order_ack != True:
                    continue
                mv.B_dist  -= PERIPH["wheels"].left_motor.position
                mv.order='straight'
                while (PERIPH["color"].color != 1):
                    continue
                mv.B_dist  += PERIPH["wheels"].left_motor.position
                mv.order='turn right'
                while mv.order_ack != True:
                    continue
                mv.C_dist  -= PERIPH["wheels"].left_motor.position
                mv.order='straight'
                while (PERIPH["color"].color != 1):
                    continue
                mv.C_dist  += PERIPH["wheels"].left_motor.position
                mv.order='turn right'
                while mv.order_ack != True:
                    continue
                mv.D_dist  -= PERIPH["wheels"].left_motor.position
                mv.order='straight'
                while (PERIPH["color"].color != 1):
                    continue
                mv.D_dist  += PERIPH["wheels"].left_motor.position
                mv.order='turn right'
                while mv.order_ack != True:
                    continue

                mv.A_dist = min(mv.A_dist,mv.C_dist)
                mv.B_dist = min(mv.D_dist,mv.B_dist)
                mv.C_dist = min(mv.A_dist,mv.C_dist)
                mv.D_dist = min(mv.D_dist,mv.B_dist)


                mv.order = 'retract'
                # print("STARTING TO RETRACT")

                while mv.pattern_done != True:
                    if sns.sonar_detected:
                        mv.order = 'stop'
                        break
                    

                mv.stop_pattern = True
                mv.end = True
                grph.end = True
                sns.sonar_enable=False
                T_sensor.join()
                T_pattern.join()
                T_graphic.join()

            # print("all processes done")
            user_cmd = 'help'


        # CALIBRATION MENU SUB-ROUTINE
        if (user_cmd.lower() == 'calibrate'):
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
            user_cmd = 'help'


        # CONFIGURATION MENU SUB-ROUTINE
        if (user_cmd.lower() == 'config'):
            menu.action = menu.configure()

            if menu.action == 'default cfg':
                init('default')
            elif menu.action == 'user cfg':
                init('user')
            elif menu.action == 'modify cfg':
                check, ERR, SYS = init_checkwheels()
                if (check == 1):
                    print("Motor ports for wheeldrive have not been modified.")
                check, ERR, SYS = init_checkclaw()
                if (check == 1):
                    print("Motor port for claw has not been modified.")
                check, ERR = init_checksensors()

                mv.init(PERIPH, SYS)
                print("Changes have been applied to the current configuration.")
                print("Press any key to dismiss.")
                input()

            elif menu.action == 'reset cfg':
                init('reset')
            elif menu.action == 'check cfg':
                print("Current configuration:")
                for key in SYS:
                    if key[1] == 'o':
                        grph.echo(" | {}\t:\n\t=> {}".format(key, SYS[key]))
                for key in SYS:
                    if key[1] == 'h':
                        grph.echo(" | {}\t:\n\t=> {}".format(key, SYS[key]))
                for key in SYS:
                    if key[1] == 'a':
                        grph.echo(" | {}\t:\n\t=> {}".format(key, SYS[key]))
                for key in SYS:
                    if key[1] == 'n':
                        grph.echo(" | {}\t:\n\t=> {}".format(key, SYS[key]))
                print("\nPress any key to dismiss.")
                input()
            user_cmd = 'help'


        # SPIN COMMAND SUB-ROUTINE
        if (user_cmd.lower() == 'spin'):
            PERIPH["wheels"].on(8,-8)
            continue


        # STOP COMMAND SUB-ROUTINE
        if (user_cmd.lower() == 'stop'):
            PERIPH["wheels"].on(0,0)
            continue
        

        # HELP MENU
        if (user_cmd.lower() == 'help'):
            grph.CLEAR_CONSOLE()
            menu.help()
            continue


        # EXIT COMMAND
        if (user_cmd.lower() == 'exit'):
            return



        # ETC COMMANDS
        if (user_cmd.lower() == ''):
            continue
        # else
        print("Invalid argument.")
        print("\n\t>>> {} is not recognized as a command.\n".format(user_cmd.lower()))


    return


# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---  ---
SYS = init()
main()

# grph.CLEAR_CONSOLE()
grph.TECHNOBOTS_LOGO('left slant')
# grph.ROBOT()

# ---  ---  ---  ---  ---