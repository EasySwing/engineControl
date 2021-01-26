import RPi.GPIO as GPIO

MOTOR_TOP = {
    'ROTATION_PIN': 17,
    'DIRECTION_PIN': 27,
    'HOME_SWITCH': 22
}

MOTOR_BOTTOM = {
    'ROTATION_PIN': 23,
    'DIRECTION_PIN': 24,
    'HOME_SWITCH': 22
}
MOTORS = [MOTOR_TOP, MOTOR_BOTTOM]

ROTATION_PULSES = 400


def setup_pins():
    GPIO.setmode(GPIO.BCM)

    for MOTOR in MOTORS:
        GPIO.setup(MOTOR.get('ROTATION_PIN'), GPIO.OUT)
        GPIO.setup(MOTOR.get('DIRECTION_PIN'), GPIO.OUT)
        GPIO.setup(MOTOR.get('HOME_SWITCH'), GPIO.OUT)