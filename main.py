import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
PIN = 24
GPIO.setup(PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(PIN, 1)
        sleep(0.5)
        GPIO.output(PIN, 0)
        sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
