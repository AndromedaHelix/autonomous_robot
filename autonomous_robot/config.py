
# All units are in meters and radians
class RobotConfig:

    def __init__(self, wheel_radius, robot_radius):
        self.wheel_radius = wheel_radius

        self.robot_radius = robot_radius

class RobotVelocity:

    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

class RobotPosition:

    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
