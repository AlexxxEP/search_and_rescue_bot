from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B
from time import sleep

# Initialize the motors connected to the claw
claw_motor_left = MediumMotor(OUTPUT_A)
claw_motor_right = MediumMotor(OUTPUT_B)

# Define functions to control the claw movement
def open_claw():
    claw_motor_left.on_for_seconds(speed=50, seconds=1)
    claw_motor_right.on_for_seconds(speed=-50, seconds=1)

def close_claw():
    claw_motor_left.on_for_seconds(speed=-50, seconds=1)
    claw_motor_right.on_for_seconds(speed=50, seconds=1)

# Test the claw movement
try:
    while True:
        open_claw()
        sleep(2)
        close_claw()
        sleep(2)

except KeyboardInterrupt:
    # Stop motors and exit cleanly on Ctrl+C
    claw_motor_left.off()
    claw_motor_right.off()
