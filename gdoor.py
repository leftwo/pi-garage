#
# Requires RPi.GPIO
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
while True:
    if (GPIO.input(23) == 1):
        print("Button 1 pressed")
    else:
	print("Button 1 released")

    sleep(1)

