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
