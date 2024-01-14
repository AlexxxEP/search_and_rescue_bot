from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep

# Initialize motors for the claw
#claw_motor_left = MediumMotor(OUTPUT_A)
claw_motor_right = MediumMotor(OUTPUT_B)

# Initialize ultrasonic sensor
ultrasonic_sensor = UltrasonicSensor()

# Define functions to control the claw movement
def open_claw():
    #claw_motor_left.on_for_seconds(speed=50, seconds=1)
    claw_motor_right.on_for_seconds(speed=-50, seconds=1)

def close_claw():
    #claw_motor_left.on_for_seconds(speed=-50, seconds=1)
    claw_motor_right.on_for_seconds(speed=50, seconds=1)



# Function to find and grab an object
def find_and_grab_object():
    try:
        while True:
            distance = ultrasonic_sensor.distance_centimeters
            print("Distance to object:", distance, "cm")

            if distance <= 10: # Adjust this distance according to your needs
                print("Object detected - grabbing...")
                close_claw()
                sleep(2) # Adjust time to hold the object
                open_claw()
                sleep(1)
                open_claw()
                break # Exit the loop after grabbing the object

    except KeyboardInterrupt:
        # Stop motors and exit cleanly on Ctrl+C
        #claw_motor_left.off()
        claw_motor_right.off()

# Run the function to find and grab an object
find_and_grab_object()
