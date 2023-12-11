from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from time import wait

#CONSTANTS
 wheel_diameter=55.5
color = ColorSensor()
wheels = MoveTank( OUTPUT_D, OUTPUT_A)
timeout = 1000

#var
timecount = 0

wait(100)
print("init")
color.calibrate_white()
wait(100)

Straight()
while (timecount < timeout):
  timecount +=1
  if (color.color = 1):
    Stop()
    wait(100)
    Turn(cw)
    print("found edge")
    wait(100)
    Stop()
    return 0
  print ("timed out")
  return 1





def Straight ( speed ):
    wheels.on(speed, speed)
    print("moving straight at", speed, "speed !")
    return

def Turn(direction):
    if (direction == "cw"):
      wheels.on(10, 0)
    else if (direction == "ccw"):
      wheels.on(0, 10)
    else:
      print("specify cw or ccw")
    return


def Stop (  ):
    wheels.on(0, 0)
    print("Stopping")
    return

