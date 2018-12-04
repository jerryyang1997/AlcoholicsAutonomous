#import modules
import RPi.GPIO as GPIO
import time

#set output pins
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

#turn on all pumps for 10 seconds
GPIO.output(PUMP1,GPIO.HIGH)
GPIO.output(PUMP2,GPIO.HIGH)
GPIO.output(PUMP3,GPIO.HIGH)
GPIO.output(PUMP4,GPIO.HIGH)
time.sleep(10)

#turn pump1 off
GPIO.output(PUMP1,GPIO.LOW)
time.sleep(5)

#turn pump2 off
GPIO.output(PUMP2,GPIO.LOW)
time.sleep(5)

#turn pump3 off
GPIO.output(PUMP3,GPIO.LOW)
time.sleep(5)

#turn pump4 off
GPIO.output(PUMP4,GPIO.LOW)

