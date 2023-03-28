import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 12, 11, 13, 15
# GPIO18, GPIO17, GPIO27, GPIO22
# IN1 - 18
# IN2 - 17
# IN3 - 27
# IN4 - 22
IN1 = 18
IN2 = 17
IN3 = 27
IN4 = 22

# Define advanced sequence
# as shown in manufacturers datasheet
#Seq = [[1,0,0,1],
#       [1,0,0,0],
#       [1,1,0,0],
#       [0,1,0,0],
#       [0,1,1,0],
#       [0,0,1,0],
#       [0,0,1,1],
#       [0,0,0,1]]

Seq = [[1,0,1,0],
       [1,0,0,1],
       [0,1,0,1],
       [0,1,1,0]]

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def setStep(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)

def rotate(deg, direction):
    if direction == "ccw":
        Seq = Seq[::-1]
    steps = deg // 5.625 # 1/64 of a revolution
    for i in range(steps):
        for j in range(4):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(0.001)

try:
    rotate(2048, "cw")
    time.sleep(1)
    rotate(2048, "ccw")
    time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
