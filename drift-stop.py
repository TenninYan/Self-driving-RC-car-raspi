#!/usr/bin/env python

import socket
import RPi.GPIO as GPIO
import time
import sys


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

TCP_IP = 'tenyPi.local'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
data_old = "stop"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

up = GPIO.PWM(Port_list[0], 200)
down = GPIO.PWM(Port_list[1], 200)
right = GPIO.PWM(Port_list[2], 200)
up.start(0)
down.start(0)
right.start(0)
print "Up false"

data=""
s.listen(1)
conn, addr = s.accept()
print 'Connection address:', addr

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    #if not data==data_old: break
    print "received data:", data

    #while True:
    if not data==data_old:
        if data=="exit":
            up.stop()
            down.stop()
            right.stop()
            GPIO.cleanup()
            conn.close()
            sys.exit()
        elif data=="stop":
            right.ChangeDutyCycle(100)
            time.sleep(0.5)
            up.ChangeDutyCycle(0)
            time.sleep(0.1)
            down.ChangeDutyCycle(100)
            time.sleep(1)
            down.ChangeDutyCycle(0)
            right.ChangeDutyCycle(0)
            print "Up False"
            up.stop()
            down.stop()
            right.stop()
            GPIO.cleanup()
            conn.close()
            sys.exit()
        elif data=="go":
            up.ChangeDutyCycle(100)
            print "Up true"
            data_old = data
        else:
            print "Unknown"


