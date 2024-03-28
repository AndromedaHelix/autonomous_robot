# Written by Juan Pablo Gutiérrez
from typing import List
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist

from autonomous_robot.motor import Motor

from autonomous_robot.config import *
from autonomous_robot.kinematics import Kinematics


class HolonomicRobot:
    def __init__(self, motor1 : Motor, motor2 : Motor, motor3 : Motor, motor4 : Motor):
    
        self.Kinematics = Kinematics(RobotConfig(0.05, 0.14))
        
        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.motor4 = motor4

    
    def moveRobot (self, movement : Twist):
        print("Moving Motor")
        
        wheel_velocities : List[float] = self.Kinematics.getWheelsAngularVelocities(RobotVelocity(movement.linear.x , movement.linear.y, movement.angular.z), RobotPosition(0, 0, 0))
        
        self.motor1.moveMotor(wheel_velocities[0])
        self.motor2.moveMotor(wheel_velocities[1])
        self.motor3.moveMotor(wheel_velocities[2])
        self.motor4.moveMotor(wheel_velocities[3])
        
        return ', '.join(map(str, wheel_velocities))

