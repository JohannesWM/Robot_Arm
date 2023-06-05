import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin number
out1 = 17
out2 = 18
out3 = 27
out4 = 22

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002

step_count = 200

# setting up
GPIO.setmode(GPIO.BCM)
GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)
GPIO.setup(out4, GPIO.OUT)

# initializing
GPIO.output(out1, GPIO.LOW)
GPIO.output(out2, GPIO.LOW)
GPIO.output(out3, GPIO.LOW)
GPIO.output(out4, GPIO.LOW)

servo_pin = 5

# Set up the GPIO pin for servo control
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance with a frequency of 50Hz
pwm = GPIO.PWM(servo_pin, 50)


# Function to move the servo to a specified angle
def move_servo(angle):
  duty_cycle = (angle / 18) + 2
  pwm.ChangeDutyCycle(duty_cycle)
  time.sleep(0.3)  # Adjust the delay as needed for your servo


# Main program loop
try:
  pwm.start(0)

  while True:
    # Move the servo from 0 to 180 degrees
    for angle in range(0, 181, 1):
      move_servo(angle)

    time.sleep(1)  # Pause for 1 second at 180 degrees

    # Move the servo from 180 to 0 degrees
    for angle in range(180, -1, -1):
      move_servo(angle)

    time.sleep(1)  # Pause for 1 second at 0 degrees

except KeyboardInterrupt:
  pass

# Clean up GPIO settings
pwm.stop()
GPIO.cleanup()
