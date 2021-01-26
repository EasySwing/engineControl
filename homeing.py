import RPi.GPIO as GPIO
from time import sleep

from config import setup_pins, MOTORS

setup_pins()

def home_yet(PIN):
    return GPIO.input(PIN)

try:
    for motor in MOTORS:
        while True:
            GPIO.output(motor.get('ROTATION_PIN'), 1)
            sleep(0.001)
            GPIO.output(motor.get('ROTATION_PIN'), 0)
            sleep(0.001)

            if home_yet(motor.get('HOME_SWITCH')):
                print('home! :)')
                break


except KeyboardInterrupt:
    GPIO.cleanup()
