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

print "GPIO started"
#On_Off_list = [0,0,0,0]

#while True:
#    x = getch()
#    a = str(x)
#
#    if a=="q":
#        GPIO.cleanup()
#        sys.exit()
#    elif a=="\x1b[A" or a=="w" or a=="k":
#            GPIO.output(Port_list[0],True)
#            print "Up true"
#            time.sleep(0.5)
#            #On_Off_list[0] = 1
#    elif a=='\x1b[B' or a=="s" or a=="j":
#            GPIO.output(Port_list[1],True)
#            print "Down true"
#            time.sleep(0.5)
#            #On_Off_list[1] = 1
#    elif a=='\x1b[C' or a=="d" or a=="l":
#            GPIO.output(Port_list[2],True)
#            print "Right true"
#            time.sleep(0.5)
#            #On_Off_list[2] = 1
#    elif a=='\x1b[D' or a=="a" or a=="h":
#            GPIO.output(Port_list[3],True)
#            print "Left true"
#            time.sleep(0.5)
#            #On_Off_list[3] = 1
#    else:
#        print "Unknown"
#
#
#    GPIO.output(Port_list[0],False)
#    GPIO.output(Port_list[1],False)
#    GPIO.output(Port_list[2],False)
#    GPIO.output(Port_list[3],False)
