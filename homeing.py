import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
ROTATION_PIN = 17
DIRECTION_PIN = 27
HOME = 22
GPIO.setup(ROTATION_PIN, GPIO.OUT)
GPIO.setup(DIRECTION_PIN, GPIO.OUT)
GPIO.setup(HOME, GPIO.OUT)

ROTATION_PULSES = 400

try:
    while True:
        GPIO.output(ROTATION_PIN, 1)
        sleep(0.001)
        GPIO.output(ROTATION_PIN, 0)
        sleep(0.001)

        home_yet = GPIO.input(HOME)
        print(home_yet)
        if home_yet:
            break


except KeyboardInterrupt:
    GPIO.cleanup()
