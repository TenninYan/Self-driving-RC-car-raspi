#!/usr/bin/env python

import socket
import RPi.GPIO as GPIO
import time

import sys   


GPIO.setmode(GPIO.BOARD)
#up
GPIO.setup(11, GPIO.OUT)
#down
GPIO.setup(13, GPIO.OUT)
#right
GPIO.setup(15, GPIO.OUT)
#left
GPIO.setup(16, GPIO.OUT)

Port_list = [11,13,15,16]
On_Off_list = [0,0,0,0]

#TCP_IP = '157.82.5.182'
TCP_IP = 'tenyPi.local'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data

    if data=="exit":
        GPIO.cleanup()
        sys.exit()
        conn.close()
    elif data=="stop":
            GPIO.output(Port_list[0],False)
            print "Up False"
            #On_Off_list[0] = 1
    elif data=="go":
            GPIO.output(Port_list[0],True)
            print "Up true"
            #On_Off_list[0] = 1
    else:
        print "Unknown"


    # time.sleep(0.5)
    # GPIO.output(Port_list[0],False)
    # GPIO.output(Port_list[1],False)
   # GPIO.output(Port_list[2],False)
   # GPIO.output(Port_list[3],False)



