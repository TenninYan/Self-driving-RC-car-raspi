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
#On_Off_list = [0,0,0,0]

GPIO.output(Port_list[0],True)
print "Up true"
time.sleep(0.5)
##On_Off_list[0] = 1
#GPIO.output(Port_list[1],True)
#print "Down true"
#time.sleep(0.5)
##On_Off_list[1] = 1
#GPIO.output(Port_list[2],True)
#print "Right true"
#time.sleep(0.5)
##On_Off_list[2] = 1
#GPIO.output(Port_list[3],True)
#print "Left true"
#time.sleep(0.5)
##On_Off_list[3] = 1


GPIO.output(Port_list[0],False)
GPIO.output(Port_list[1],False)
GPIO.output(Port_list[2],False)
GPIO.output(Port_list[3],False)


#for x in range(0,5):
#    GPIO.output(7,True)
#    time.sleep(.5)
#    GPIO.output(7,False)
#    GPIO.output(11,True)
#    time.sleep(.5)
#    GPIO.output(11,False)
#    GPIO.output(13,True)
#    time.sleep(.5)
#    GPIO.output(13,False)
#    GPIO.output(15,True)
#    time.sleep(.5)
#    GPIO.output(15,False)
