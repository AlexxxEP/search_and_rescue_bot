from ev3dev2.motor import *
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

# Initialize motors for movement
right_motor = MoveTank(OUTPUT_D, OUTPUT_A)
#right_motor = LargeMotor(OUTPUT_C)

# Initialize color sensor
color_sensor = ColorSensor()

# Constants for the robot's movements
wheel_diameter = 5.6 # Diameter of the wheels in centimeters
wheel_circumference = wheel_diameter * 3.1416 # Circumference = π * diameter
wheel_distance = 12.5 # Distance between the wheels in centimeters

# Calculate the number of rotations needed for the robot to move forward by 1.5 meters
# Distance traveled = Number of rotations * Wheel circumference
distance_to_travel = 150 # 1.5 meters = 150 centimeters
rotations_needed = distance_to_travel / wheel_circumference

# Function to make the robot move forward by a given number of rotations
def move_forward():
    #left_motor.on_for_rotations(speed=20, rotations=rotations_needed)
    right_motor.on_for_rotations(20, rotations_needed,10)

# Function to make the robot turn right
def turn_right():
    #left_motor.on_for_rotations(speed=20, rotations=rotations_needed / 2)
    right_motor.on_for_rotations(-20, rotations_needed / 2,10)

# Function to make the robot turn left
def turn_left():
    #left_motor.on_for_rotations(speed=-20, rotations=rotations_needed / 2)
    right_motor.on_for_rotations(0, rotations_needed / 2,0.25)

try:
    # Explore the 1.5x1.5 meters square zone in a snake pattern
    for _ in range(2): # Repeat the pattern twice to cover the square
        move_forward()
        color = color_sensor.color # Get the detected color
        if color == ColorSensor.COLOR_BLACK: # Modify according to the desired color
            turn_right()
        elif color == ColorSensor.COLOR_WHITE: # Modify according to the desired color
            turn_left()

except KeyboardInterrupt:
    # Stop motors and exit cleanly on Ctrl+C
    left_motor.off()
    right_motor.off()
