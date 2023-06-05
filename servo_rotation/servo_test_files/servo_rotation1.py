import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin number
GPIO.setmode(GPIO.BOARD)
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
