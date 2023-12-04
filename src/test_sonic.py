#!/usr/bin/env python3
import socket
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep

# 设置服务器的 IP 地址和端口
SERVER_IP = '172.20.10.2'
SERVER_PORT = 12345

# 初始化超声波传感器
us = UltrasonicSensor()
us.mode = 'US-DIST-CM'

# 创建 socket 对象
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 连接到服务器
    s.connect((SERVER_IP, SERVER_PORT))
    
    try:
        while True:
            # 读取距离
            distance = us.distance_centimeters
            # 发送数据
            s.sendall(str(distance).encode('utf-8'))
            sleep(0.5)
    except KeyboardInterrupt:
        print("Program terminated")
