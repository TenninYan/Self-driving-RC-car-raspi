#!/usr/bin/env python

import socket
import RPi.GPIO as GPIO
import time

import sys   

level1 = 20
level2 = 30
level3 = 70
start_speed = 25
go_speed = 17
go_speed2 = 30

GPIO.setmode(GPIO.BOARD)
Port_list = [11,13,16,15]
#up
GPIO.setup(Port_list[0], GPIO.OUT)
#down
GPIO.setup(Port_list[1], GPIO.OUT)
#right
GPIO.setup(Port_list[2], GPIO.OUT)
#left
GPIO.setup(Port_list[3], GPIO.OUT)

#TCP_IP = '157.82.5.182'
TCP_IP = 'tenyPi.local'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
data_old = "stop"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

up = GPIO.PWM(Port_list[0], 200)
down = GPIO.PWM(Port_list[1], 200)
right = GPIO.PWM(Port_list[2], 200)
left = GPIO.PWM(Port_list[3], 200)
up.start(0)
down.start(0)
left.start(0)
right.start(0)
print "Up false"
num = 0
data=""
s.listen(1)
conn, addr = s.accept()
print 'Connection address:', addr

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    #if not data==data_old: break
    print "received data:", data
    if num == 0:
        up.ChangeDutyCycle(start_speed)
        time.sleep(1)
        num += 1

    #while True:
    if not data==data_old:
        up.ChangeDutyCycle(0)
        down.ChangeDutyCycle(0)
        right.ChangeDutyCycle(0)
        left.ChangeDutyCycle(0)
        if data=="exit":
            up.stop()
            down.stop()
            right.stop()
            left.stop()
            GPIO.cleanup()
            conn.close()
            sys.exit()
        elif data=="stop":
            p.ChangeDutyCycle(0)
        elif data=="go":
            up.ChangeDutyCycle(go_speed)
        elif data=="r1":
            up.ChangeDutyCycle(go_speed)
            right.ChangeDutyCycle(level1)
        elif data=="r2":
            up.ChangeDutyCycle(go_speed)
            right.ChangeDutyCycle(level2)
        elif data=="r3":
            up.ChangeDutyCycle(go_speed2)
            right.ChangeDutyCycle(level3)
        elif data=="l1":
            up.ChangeDutyCycle(go_speed)
            left.ChangeDutyCycle(level1)
        elif data=="l2":
            up.ChangeDutyCycle(go_speed)
            left.ChangeDutyCycle(level2)
        elif data=="l3":
            up.ChangeDutyCycle(go_speed2)
            left.ChangeDutyCycle(level3)
        else:
            up.ChangeDutyCycle()
            print "Unknown"
        data_old = data
