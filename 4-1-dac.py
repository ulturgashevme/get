import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

for i in range(8): GPIO.setup(dac[i], GPIO.OUT)

try:
    while(True):
        x = input("Write number")
        try: 
            x = int(x)
            if 0 <= x <= 255:
                for i in range(8): GPIO.output(dac[i], dec2bin(x)[i])
                volt = float(x)/255*3.3
                print("Volt: ", volt)
            else:
                if (x < 0):   print("Number < 0")
                if (x > 255): print("Number > 255")
        except Exception:
            if x == "q": break
            print("NOT number")
finally:
    for i in range(8): GPIO.output(dac[i], 0)
    GPIO.cleanup()
    print("The end!")