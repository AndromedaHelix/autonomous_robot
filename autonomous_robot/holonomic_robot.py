# Written by Juan Pablo Gutiérrez

import RPi.GPIO as GPIO
from geometry_msgs.msg import Vector3

from autonomous_robot.motor import Motor

class HolonomicRobot:
    def __init__(self, motor1 : Motor, motor2 : Motor, motor3 : Motor, motor4 : Motor):
        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.motor4 = motor4
    
    def moveRobot (self, movement : Vector3):
        print("Moving Motor")
        self.motor1.moveMotor(movement)
        self.motor2.moveMotor(movement)
        self.motor3.moveMotor(movement)
        self.motor4.moveMotor(movement)

