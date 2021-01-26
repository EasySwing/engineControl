import RPi.GPIO as GPIO
from time import sleep

from config import setup_pins, ROTATION_PULSES, MOTORS

setup_pins()

try:
    for motor in MOTORS:
        for i in range(0, ROTATION_PULSES):
            GPIO.output(motor.get('ROTATION_PIN'), 1)
            sleep(0.001)
            GPIO.output(motor.get('ROTATION_PIN'), 0)
            sleep(0.001)

        for i in range(0, ROTATION_PULSES * 2):
            GPIO.output(motor.get('DIRECTION_PIN'), 1)
            GPIO.output(motor.get('ROTATION_PIN'), 1)
            sleep(0.001)
            GPIO.output(motor.get('ROTATION_PIN'), 0)
            sleep(0.001)
            GPIO.output(motor.get('DIRECTION_PIN'), 0)


except KeyboardInterrupt:
    GPIO.cleanup()
