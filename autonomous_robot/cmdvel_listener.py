#Written by Juan Pablo Gutiérrez

import rclpy 
from rclpy.node import Node

from geometry_msgs.msg import Twist

class CmdVelListener(Node): 
    def __init__(self):
        super().__init__('cmdvel_listener')
        self.subscription = self.create_subscription(
            Twist,
            'cmdvel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
    def listener_callback(self, msg:Twist):
        self.get_logger().info('I heard: "%s"' % msg._linear)

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