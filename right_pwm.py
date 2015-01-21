import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

up = GPIO.PWM(11, 200)
right = GPIO.PWM(16, 200)
up.start(25)
time.sleep(1)

up.start(18)

right.start(20)
print "left 20"
time.sleep(2)

right.start(30)
print "left 30"
time.sleep(2)

#right.start(70)
#up.start(30)
#print "left 70"
#time.sleep(2)

#right.start(100)
#print "left 100"
#time.sleep(2)
#input('Press return to stop:')   # use raw_input for Python 2
up.stop()
right.stop()
GPIO.cleanup()
