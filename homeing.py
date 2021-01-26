import RPi.GPIO as GPIO
from time import sleep

from config import setup_pins, ROTATION_PULSES

setup_pins()

def home_yet(PIN):
    return GPIO.input(PIN)

try:
    while True:
        GPIO.output(ROTATION_PIN, 1)
        sleep(0.001)
        GPIO.output(ROTATION_PIN, 0)
        sleep(0.001)

        if home_yet(HOME):
            print('home! :)')
            break


except KeyboardInterrupt:
    GPIO.cleanup()
