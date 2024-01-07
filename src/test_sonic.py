#!/usr/bin/env python3
import socket
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep


SERVER_IP = '172.20.10.2'
SERVER_PORT = 12345

us = UltrasonicSensor()
us.mode = 'US-DIST-CM'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    
    try:
        while True:
            distance = us.distance_centimeters
            s.sendall(str(distance).encode('utf-8'))
            sleep(0.5)
    except KeyboardInterrupt:
        print("Program terminated")
