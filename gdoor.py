#!/usr/bin/python
# Requires RPi.GPIO
from time import sleep
import RPi.GPIO as GPIO

# XXX Move constants to config file, import that.
# XXX Add logging to console.

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


def get_state():
    """ Read the state of the door switch """
    if (GPIO.input(23) == 1):
        return 1
    return 0


if __name__ == '__main__':
    setup()
    state = get_state()

    print "Starting with state ", state

    while True:
        new_state = get_state()
        if (new_state != state):
	    print "state change to ", new_state
	    state = new_state
 
        sleep(1)

