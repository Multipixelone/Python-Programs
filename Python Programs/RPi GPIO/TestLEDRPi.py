import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(12,True)

while True:
	GPIO.output(11,True)
	GPIO.output(15,True)
	time.sleep(1)
	GPIO.output(11,False)
	GPIO.output(15,False)
        time.sleep(1)

