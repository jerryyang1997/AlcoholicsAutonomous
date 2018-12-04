#import modules
import RPi.GPIO as GPIO
import time

#declare output pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PUMP1 = 6
PUMP2 = 27
PUMP3 = 17
PUMP4 = 5

GPIO.setup(PUMP1, GPIO.OUT)
GPIO.setup(PUMP2, GPIO.OUT)
GPIO.setup(PUMP3, GPIO.OUT)
GPIO.setup(PUMP4, GPIO.OUT)

#turn pumps 1 and 4 on for 5 seconds and turn them off
GPIO.output(PUMP1,GPIO.HIGH)
GPIO.output(PUMP4,GPIO.HIGH)
time.sleep(5)
GPIO.output(PUMP1,GPIO.LOW)
GPIO.output(PUMP4,GPIO.LOW)

#turn pumps 2 and 3 on for 5 seconds and turn them off
GPIO.output(PUMP2,GPIO.HIGH)
GPIO.output(PUMP3,GPIO.HIGH)
time.sleep(5)
GPIO.output(PUMP3,GPIO.LOW)
GPIO.output(PUMP2,GPIO.LOW)

#turn pump 1 on for 2 seconds and turn it off
GPIO.output(PUMP1,GPIO.HIGH)
time.sleep(2)
GPIO.output(PUMP1,GPIO.LOW)

#turn pump 2 on for 2 seconds and turn it off
GPIO.output(PUMP2,GPIO.HIGH)
time.sleep(2)
GPIO.output(PUMP2,GPIO.LOW)

#turn pump 3 on for 2 seconds and turn it off
GPIO.output(PUMP3,GPIO.HIGH)
time.sleep(2)
GPIO.output(PUMP3,GPIO.LOW)

#turn pump4 on for 2 seconds and turn it off
GPIO.output(PUMP4,GPIO.HIGH)
time.sleep(2)
GPIO.output(PUMP4,GPIO.LOW)
