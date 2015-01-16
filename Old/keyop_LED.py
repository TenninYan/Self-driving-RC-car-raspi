import RPi.GPIO as GPIO
import time

import sys

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

GPIO.setmode(GPIO.BOARD)
#up
GPIO.setup(7, GPIO.OUT)
#down
GPIO.setup(11, GPIO.OUT)
#right
GPIO.setup(13, GPIO.OUT)
#left
GPIO.setup(15, GPIO.OUT)

Port_list = [7,11,13,15]
On_Off_list = [0,0,0,0]

while True:
    getch = _Getch()
    x = getch()
    a = str(x)

    if a=="q":
        GPIO.cleanup()
        sys.exit()
    elif a=="\x1b[A" or a=="w" or a=="k":
        if On_Off_list[0] == 0:
            GPIO.output(Port_list[0],True)
            print "Up true"
            On_Off_list[0] = 1
        else:
            GPIO.output(Port_list[0],False)
            print "Up false"
            On_Off_list[0] = 0
    elif a=='\x1b[B' or a=="s" or a=="j":
        if On_Off_list[1] == 0:
            GPIO.output(Port_list[1],True)
            print "Down true"
            On_Off_list[1] = 1
        else:
            GPIO.output(Port_list[1],False)
            print "Down false"
            On_Off_list[1] = 0
    elif a=='\x1b[C' or a=="d" or a=="l":
        if On_Off_list[2] == 0:
            GPIO.output(Port_list[2],True)
            print "Right true"
            On_Off_list[2] = 1
        else:
            GPIO.output(Port_list[2],False)
            print "Right false"
            On_Off_list[2] = 0
    elif a=='\x1b[D' or a=="a" or a=="h":
        if On_Off_list[3] == 0:
            GPIO.output(Port_list[3],True)
            print "Left true"
            On_Off_list[3] = 1
        else:
            GPIO.output(Port_list[3],False)
            print "Left false"
            On_Off_list[3] = 0
    else:
        print "Unknown"


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
