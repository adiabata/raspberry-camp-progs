import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

while True:
     if GPIO.input(14) == True:
          print('I LOVE MINECRAFT')
          time.sleep(0.5)