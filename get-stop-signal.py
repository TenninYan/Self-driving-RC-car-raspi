#!/usr/bin/env python

import socket
import RPi.GPIO as GPIO
import time

import sys   


GPIO.setmode(GPIO.BOARD)
Port_list = [11,13,15,16]
#up
GPIO.setup(Port_list[0], GPIO.OUT)
#down
GPIO.setup(Port_list[1], GPIO.OUT)
#right
GPIO.setup(Port_list[2], GPIO.OUT)
#left
GPIO.setup(Port_list[3], GPIO.OUT)


GPIO.output(Port_list[0],True)
GPIO.output(Port_list[1],True)
print "Up true"

#TCP_IP = '157.82.5.182'
TCP_IP = 'tenyPi.local'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
data_old = "none"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

while True:
    data=""
    time.sleep(1)
    s.listen(1)
    conn, addr = s.accept()
    print 'Connection address:', addr
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    #if not data==data_old: break
    print "received data:", data

    #while True:
    if not data==data_old:
        if data=="exit":
            GPIO.cleanup()
            conn.close()
            sys.exit()
        elif data=="stop":
                GPIO.output(Port_list[0],False)
                GPIO.output(Port_list[1],False)
                print "Up False"
                data_old = data
        elif data=="go":
                GPIO.output(Port_list[0],True)
                GPIO.output(Port_list[1],True)
                print "Up true"
                data_old = data
        else:
            print "Unknown"
