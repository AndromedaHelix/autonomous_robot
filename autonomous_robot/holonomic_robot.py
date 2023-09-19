# Written by Juan Pablo Gutiérrez

import RPi.GPIO as GPIO

from geometry_msgs.msg import Vector3


class HolonomicRobot:
    def __init__(self, IN1A, IN1B, PWM1, IN2A, IN2B, PWM2, IN3A, IN3B, PWM3, IN4A, IN4B, PWM4):
        self.IN1A = IN1A
        self.IN1B = IN1B
        self.PWM1 = PWM1
        self.IN2A = IN2A
        self.IN2B = IN2B
        self.PWM2 = PWM2
        self.IN3A = IN3A
        self.IN3B = IN3B
        self.PWM3 = PWM3
        self.IN4A = IN4A
        self.IN4B = IN4B
        self.PWM4 = PWM4

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # Setting GPIO pins for all motors pins
        GPIO.setup(self.IN1A, GPIO.OUT) 
        GPIO.setup(self.IN1B, GPIO.OUT) 
        GPIO.setup(self.PWM1, GPIO.OUT) 

        GPIO.setup(self.IN2A, GPIO.OUT) 
        GPIO.setup(self.IN2B, GPIO.OUT) 
        GPIO.setup(self.PWM2, GPIO.OUT) 

        GPIO.setup(self.IN3A, GPIO.OUT) 
        GPIO.setup(self.IN3B, GPIO.OUT) 
        GPIO.setup(self.PWM3, GPIO.OUT) 

        GPIO.setup(self.IN4A, GPIO.OUT) 
        GPIO.setup(self.IN4B, GPIO.OUT) 
        GPIO.setup(self.PWM4, GPIO.OUT)

        # Starting PWM 
        self.pwm1 : GPIO.PWM = GPIO.PWM(self.PWM1, 100)
        self.pwm1.start(0)

        self.pwm2 : GPIO.PWM = GPIO.PWM(self.PWM2, 100)
        self.pwm2.start(0)

        self.pwm3 : GPIO.PWM = GPIO.PWM(self.PWM3, 100)
        self.pwm3.start(0)

        self.pwm4 : GPIO.PWM = GPIO.PWM(self.PWM4, 100)
        self.pwm4.start(0)
    
    def moveMotor (movement : Vector3):
        print("Moving Motor")

    def inverMotor(self, motor : int):
        # switch statement for 4 motors

        # TODO CREATE MOTOR CLASS AND MOVE THIS METHOD TO IT
        match motor:
            case 1:
                GPIO.output(self.IN1A, GPIO.LOW) # Set AIN1
                GPIO.output(self.IN1B, GPIO.HIGH) # Set AIN2
            case 2:
                GPIO.output(self.IN2A, GPIO.LOW) # Set AIN1
                GPIO.output(self.IN2B, GPIO.HIGH) # Set AIN2
            case 3:
                GPIO.output(self.IN3A, GPIO.LOW) # Set AIN1
                GPIO.output(self.IN3B, GPIO.HIGH) # Set AIN2
            case 4:
                GPIO.output(self.IN4A, GPIO.LOW) # Set AIN1
                GPIO.output(self.IN4B, GPIO.HIGH) # Set AIN2




