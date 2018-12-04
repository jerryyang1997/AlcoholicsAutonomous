import RPi.GPIO as GPIO
import time

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

GPIO.output(PUMP1,GPIO.HIGH)
GPIO.output(PUMP2,GPIO.HIGH)
GPIO.output(PUMP3,GPIO.HIGH)
GPIO.output(PUMP4,GPIO.HIGH)
time.sleep(10)
GPIO.output(PUMP1,GPIO.LOW)
time.sleep(5)
GPIO.output(PUMP2,GPIO.LOW)
time.sleep(5)
GPIO.output(PUMP3,GPIO.LOW)
time.sleep(5)
GPIO.output(PUMP4,GPIO.LOW)

