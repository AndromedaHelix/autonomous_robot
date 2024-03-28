#Written by Juan Pablo Gutiérrez

import rclpy 
from rclpy.node import Node

from geometry_msgs.msg import Twist

from autonomous_robot.holonomic_robot import HolonomicRobot
from autonomous_robot.motor import Motor

class CmdVelListener(Node): 
    def __init__(self):
        super().__init__('velocity_listener')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.robot = HolonomicRobot(
            Motor(36, 38, 32, False), # Wheel 1 -- CW
            Motor(10, 12, 8, True),  # Wheel 2 -- CCW
            Motor(13, 15, 16, True),  # Wheel 3 -- CCW
            Motor(35, 37, 31, False),  # Wheel 4 -- CW
        ) 
              
    def listener_callback(self, msg : Twist):
        x = self.robot.moveRobot(msg)
        self.get_logger().info('I heard: "%s,"' % (x))

def main(args=None):
    rclpy.init(args=args)

    cmdvel_listener = CmdVelListener()

    rclpy.spin(cmdvel_listener)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    cmdvel_listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()