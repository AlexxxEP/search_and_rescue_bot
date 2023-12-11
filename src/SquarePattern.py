print("Helloworld")


from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from time import sleep

#CONSTANTS
gyro = GyroSensor()
wheel_diameter=55.5
color = ColorSensor()
wheels = MoveTank( OUTPUT_D, OUTPUT_A)
timeout = 3000

#var
#current_ang= 0
timecount = 0



def Straight ( speed ):
    wheels.on(speed, speed)
    print("moving straight at", speed, "speed !")
    return

def Turn(direction):
    current_ang = gyro.angle
    timecounter = 0
    if (direction == "cw"):
        while (current_ang >= gyro.angle + 90 or current_ang <= gyro.angle -90):
            timecounter +=1
            print(gyro.angle)
            wheels.on(10, -10)
            if(timecounter == timeout):
                break
        Stop()
        return
    elif (direction == "ccw"):
         while (current_ang >= gyro.angle + 90 or current_ang <= gyro.angle -90):
             timecounter +=1
             print(gyro.angle)
             wheels.on(-10, 10)
             if(timecounter == timeout):
                break
         Stop()
         return
    else:
      print("specify cw or ccw")
    return


def Stop (  ):
    wheels.on(0, 0)
    print("Stopping")
    return






# MAINSCRIPT
sleep(1)
print("Init: DO NOT MOVE")
gyro.calibrate
color.calibrate_white()

sleep(1)


#Straight(50)
#while (timecount < timeout):
  #timecount +=1
  #if (color.color == 1):
Stop()
rint("found edge")
sleep(1)
Turn("cw")
sleep(10)
Stop()
    #break
  #if (timecount == timeout -2):
      #print ("timed out")
    #Stop()

