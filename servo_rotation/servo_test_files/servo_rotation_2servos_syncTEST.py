import RPi.GPIO as GPIO
import time

servoPIN = 5
servo2PIN = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servo2PIN, GPIO.OUT)

z = GPIO.PWM(servo2PIN, 50) # GPIO 17 for PWM with 50Hz
z.start(2.5) # Initialization
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    z.ChangeDutyCycle(12.5)

except KeyboardInterrupt:
  p.stop()
  z.stop()
  GPIO.cleanup()