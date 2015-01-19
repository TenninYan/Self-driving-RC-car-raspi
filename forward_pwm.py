import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 50)
p.start(15)
time.sleep(5)
#p.start(30)
#time.sleep(1.5)
#p.start(70)
#time.sleep(1.5)
#p.start(100)
#time.sleep(1.5)
#input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()
