import RPi.GPIO as GPIO
import time

import sys

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
#up
GPIO.setup(11, GPIO.OUT)
#down
GPIO.setup(13, GPIO.OUT)
#right
GPIO.setup(15, GPIO.OUT)
#left
GPIO.setup(16, GPIO.OUT)

Port_list = [11,13,15,16]

GPIO.output(Port_list[0],False)
GPIO.output(Port_list[1],False)
GPIO.output(Port_list[2],False)
GPIO.output(Port_list[3],False)

GPIO.cleanup()
sys.exit()


