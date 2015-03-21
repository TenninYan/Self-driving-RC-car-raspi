# this program is made for test if radio-controlled car works
# run this program in raspberry pi (sudo python car_safe_keyop)
# then your keyboard will be controller!
# you can control in fps game style w(upward) s(backward) a(leftward) d(rightward)
# or vim style  k(upward) j(backward) h(leftward) l(rightward)
# the car moves 0.5seconds then it will stop
# press q to quit
#
# correspond pin number with your raspberry pi pin you use
# defult is 11<-upward 13<-downward 16<-leftward 15<-rightward


import RPi.GPIO as GPIO
import time
import sys
import get_one_word as word

# raspberry pi port in up,down,right,left order
Port_list = [11,13,16,15]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Port_list[0], GPIO.OUT)
GPIO.setup(Port_list[1], GPIO.OUT)
GPIO.setup(Port_list[2], GPIO.OUT)
GPIO.setup(Port_list[3], GPIO.OUT)

while True:
    getch = word._Getch()
    x = getch()
    a = str(x)

    #quit
    if a=="q":
        GPIO.cleanup()
        sys.exit()

    #upward
    elif a=="w" or a=="k":
        GPIO.output(Port_list[0],True)
        print "Up true"
        time.sleep(0.5)
    #downward
    elif a=="s" or a=="j":
        GPIO.output(Port_list[1],True)
        print "Down true"
        time.sleep(0.5)
    #rightward
    elif a=="d" or a=="l":
        GPIO.output(Port_list[2],True)
        print "Right true"
        time.sleep(0.5)
    #leftward
    elif a=="a" or a=="h":
        GPIO.output(Port_list[3],True)
        print "Left true"
        time.sleep(0.5)
    else:
        print "Unknown"

    GPIO.output(Port_list[0],False)
    GPIO.output(Port_list[1],False)
    GPIO.output(Port_list[2],False)
    GPIO.output(Port_list[3],False)
