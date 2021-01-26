import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
PIN = 17
GPIO.setup(PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(PIN, 1)

except KeyboardInterrupt:
    GPIO.cleanup()

