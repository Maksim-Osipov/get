import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
stats = 0
peroid = 1.0
while True:
    GPIO.output(led, state)
    state = not state
    time.sleep(period)