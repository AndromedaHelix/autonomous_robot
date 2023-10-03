#Written by Juan Pablo Gutiérrez

import rclpy 
from rclpy.node import Node

from geometry_msgs.msg import Vector3

import RPi.GPIO as GPIO

from autonomous_robot.holonomic_robot import HolonomicRobot
from autonomous_robot.motor import Motor

class CmdVelListener(Node): 
    def __init__(self):
        super().__init__('robot_cmdvel')
        self.subscription = self.create_subscription(
            Vector3,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.robot = HolonomicRobot(
            Motor(37, 36, 40, False), 
            Motor(35, 33, 38, True), 
            Motor(10, 12, 5, False), 
            Motor(7, 8, 3, True))
              
    def listener_callback(self, msg : Vector3):
        self.robot.moveRobot(msg)
        self.get_logger().info('I heard: "%s, %s"' % (msg.x, msg.y))

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