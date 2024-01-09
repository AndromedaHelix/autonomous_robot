from geometry_msgs.msg import Twist
from typing import List

from autonomous_robot.robot.utils.config import *

class Kinematics :

    def __init__(self, config : RobotConfig):
        self.config = config

    def getRobotVelocity(self, wheel_velocities : List[float]) -> RobotVelocity:
        pass

    def getWheelsAngularVelocities(self, robot_velocity : RobotVelocity) -> List[float]:
        pass
   