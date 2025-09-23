import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)


tran = 6
GPIO.setup(tran, GPIO.IN)

while True:  
    state = GPIO.input(tran)
    GPIO.output(led, not state)
    #time.sleep(0.1)

