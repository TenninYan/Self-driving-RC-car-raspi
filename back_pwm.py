import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(13, 50)
p.start(15)
time.sleep(2)
#p.start(30)
#time.sleep(1.5)
#p.start(70)
#time.sleep(1.5)
#p.start(100)
#time.sleep(1.5)
#input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()
