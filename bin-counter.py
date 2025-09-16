import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

for pin in leds:
    GPIO.setup(pin, GPIO.OUT)

for pin in leds:
    GPIO.setup(pin, GPIO.LOW)

up_button = 23
down_button = 22

GPIO.setup(up_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPIO.input(up_button)>0:
        num+=1
        if num>255:
            num=255
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    if GPIO.input(down_button)>0:
        num-=1

        if num<0:
            num = 0

        print(num, dec2bin(num))

        time.sleep(sleep_time)

    binary_value = dec2bin(num)
    for i in range(8):
        GPIO.output(leds[i], binary_value[i])

    






