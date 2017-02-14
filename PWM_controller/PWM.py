import RPi.GPIO as GPIO
import time, datetime
import datetime


print "The current local date time is ",datetime.datetime.now()


Yuji_LED1 = 18
CREE_RED = 17
Yuji_LED2 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(Yuji_LED1, GPIO.OUT)
GPIO.setup(CREE_RED, GPIO.OUT)
GPIO.setup(Yuji_LED2, GPIO.OUT)

pwm_CREE_RED = GPIO.PWM(CREE_RED, 500)
pwm_CREE_RED.start(100)
pwm_Yuji_LED1 = GPIO.PWM(Yuji_LED1, 500)
pwm_Yuji_LED1.start(100)
pwm_Yuji_LED2 = GPIO.PWM(Yuji_LED2, 500)
pwm_Yuji_LED2.start(100)

while True:
	duty_s = raw_input("Enter Brigtness (0 to 100):")
	duty = int(duty_s)
	pwm_Yuji_LED1.ChangeDutyCycle(duty)
	pwm_Yuji_LED2.ChangeDutyCycle(duty)
	pwm_CREE_RED.ChangeDutyCycle(duty)
