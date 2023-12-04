#!/usr/bin/env python3
import socket
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_4
from time import sleep

SERVER_IP = '172.20.10.2'
SERVER_PORT = 12345

color_sensor = ColorSensor(INPUT_4)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    
    try:
        while True:
            color = color_sensor.color_name
            s.sendall(color.encode('utf-8'))
            sleep(0.5)
    except KeyboardInterrupt:
        print("Program terminated")
