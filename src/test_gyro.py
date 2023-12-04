#!/usr/bin/env python3

import socket
from ev3dev2.sensor.lego import GyroSensor
from time import sleep

server_ip = '172.20.10.2'
server_port = 12345

gyro = GyroSensor()
gyro.mode = 'GYRO-ANG'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

try:
    while True:
        angle = gyro.angle
        client_socket.sendall(str(angle).encode('utf-8'))
        sleep(0.5)
except KeyboardInterrupt:
    print("Program terminated")
    client_socket.close()
