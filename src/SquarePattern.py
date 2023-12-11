print("prout")


from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from time import sleep

#CONSTANTS
wheel_diameter=55.5
color = ColorSensor()
wheels = MoveTank( OUTPUT_D, OUTPUT_A)
timeout = 1000

#var
timecount = 0



def Straight ( speed ):
    wheels.on(speed, speed)
    print("moving straight at", speed, "speed !")
    return

def Turn(direction):
    if (direction == "cw"):
      wheels.on(10, -10)
    elif (direction == "ccw"):
      wheels.on(-10, 10)
    else:
      print("specify cw or ccw")
    return


def Stop (  ):
    wheels.on(0, 0)
    print("Stopping")
    return






# MAINSCRIPT
sleep(1)
print("init")
color.calibrate_white()
sleep(1)


Straight(50)
while (timecount < timeout):
  timecount +=1
  if (color.color == 1):
    Stop()
    sleep(1)
    Turn(cw)
    print("found edge")
    sleep(10)
    Stop()
    break
  if (timecount == timeout -2):
      print ("timed out")
