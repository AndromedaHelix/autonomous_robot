import RPi.GPIO as GPIO
from simple_pid import PID

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

        #PID Setup
        self.pid = PID(1, 0.1, 0.05, setpoint=1) # TODO SET CONSTANTS
        

    def moveMotor(self, angularVelocity : float):
        # PID
        control = self.pid(angularVelocity)

        # Checking if movement is less than 0, if yes, invert else keep the same value

        if control < 0:
            control = abs(control)
            self.invert()
        elif self.inverted:
            self.invert()
                
        control = max(0, min(control, 100))

        self.pwm.ChangeDutyCycle(control)
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

    def getSpeed(self):
        return self.pwm.ChangeDutyCycle(0) # TODO SET THIS TO THE REAL VALUE