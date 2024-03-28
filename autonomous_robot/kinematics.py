import numpy as np
from typing import List
import math

from autonomous_robot.config import *

class Kinematics :

    def __init__(self, config : RobotConfig):
        self.config = config

    def getRobotVelocity(self, wheel_velocities : List[float]) -> RobotVelocity:
        pass

    def getWheelsAngularVelocities(self, robot_velocity : RobotVelocity, robot_position : RobotPosition) -> List[float]:
        
        x = np.array([[-math.sin(robot_position.theta + (math.pi/4)) , math.cos(robot_position.theta + (math.pi/4)) , self.config.robot_radius ], 
                      [-math.sin(robot_position.theta + (3 * math.pi/4)) , math.cos(robot_position.theta + (3 * math.pi/4)) , self.config.robot_radius ],
                      [-math.sin(robot_position.theta + (5 * math.pi/4)) , math.cos(robot_position.theta + (5 *math.pi/4)) , self.config.robot_radius ],
                      [-math.sin(robot_position.theta + (7 * math.pi/4)) , math.cos(robot_position.theta + (7 * math.pi/4)) , self.config.robot_radius ]])
        
        vel = np.array([robot_velocity.x, robot_velocity.y, robot_velocity.theta])
        
        rad = 1 / self.config.wheel_radius
        
        result = np.dot(np.dot(x, vel), rad) 
        return result.tolist()
