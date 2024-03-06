import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

GPIO.output(21, 0)

a = GPIO.input(24)

GPIO.output(21, a)

GPIO.cleanup