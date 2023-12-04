#!/usr/bin/env python3

import socket
from ev3dev2.sensor.lego import GyroSensor
from time import sleep

# 设置服务器的 IP 地址和端口
server_ip = '172.20.10.2'
server_port = 12345

# 初始化陀螺仪传感器
gyro = GyroSensor()
gyro.mode = 'GYRO-ANG'

# 创建套接字并连接
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

try:
    while True:
        angle = gyro.angle
        # 发送数据
        client_socket.sendall(str(angle).encode('utf-8'))
        sleep(0.5)
except KeyboardInterrupt:
    print("Program terminated")
    client_socket.close()
