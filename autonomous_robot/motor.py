import RPi.GPIO as GPIO

from geometry_msgs.msg import Vector3

class Motor:

    def __init__(self, IN1, IN2, PWM, inverted):
        self.inverted = inverted

        self.IN1 = IN1
        self.IN2 = IN2
        self.PWM = PWM

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # Setting GPIO pins for all motors pins
        GPIO.setup(self.IN1, GPIO.OUT) 
        GPIO.setup(self.IN2, GPIO.OUT) 
        GPIO.setup(self.PWM, GPIO.OUT) 

        # Starting PWM 
        self.pwm : GPIO.PWM = GPIO.PWM(self.PWM, 100)
        self.pwm.start(0)

    def moveMotor(self, movement : float):
        
        # Checking if movement is less than 0, if yes, invert else keep the same value

        if movement < 0:
            movement = abs(movement)
            self.invert()
        elif self.inverted:
            self.invert()
                
        movement = max(0, min(movement, 100))

        self.pwm.ChangeDutyCycle(movement)
        if self.inverted:
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
        else :
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
    
    def invert(self):
        self.inverted = not self.inverted