import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
ROTATION_PIN = 17
DIRECTION_PIN = 27
GPIO.setup(ROTATION_PIN, GPIO.OUT)
GPIO.setup(DIRECTION_PIN, GPIO.OUT)

ROTATION_PULSES = 400

try:
    for i in range(0, ROTATION_PULSES):
        GPIO.output(ROTATION_PIN, 1)
        sleep(0.001)
        GPIO.output(ROTATION_PIN, 0)
        sleep(0.001)

    for i in range(0, ROTATION_PULSES * 2):
        GPIO.output(DIRECTION_PIN, 1)
        GPIO.output(ROTATION_PIN, 1)
        sleep(0.001)
        GPIO.output(ROTATION_PIN, 0)
        sleep(0.001)
        GPIO.output(DIRECTION_PIN, 0)


except KeyboardInterrupt:
    GPIO.cleanup()
