#!/usr/bin/env python3
import socket
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_4
from time import sleep

# 设置服务器的 IP 地址和端口
SERVER_IP = '172.20.10.2'
SERVER_PORT = 12345

# 初始化颜色传感器
color_sensor = ColorSensor(INPUT_4)

# 创建 socket 对象
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 连接到服务器
    s.connect((SERVER_IP, SERVER_PORT))
    
    try:
        while True:
            # 读取颜色
            color = color_sensor.color_name
            # 发送数据
            s.sendall(color.encode('utf-8'))
            sleep(0.5)
    except KeyboardInterrupt:
        print("Program terminated")
