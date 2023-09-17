#Written by Juan Pablo Gutiérrez

import rclpy 
from rclpy.node import Node

from geometry_msgs.msg import Vector3

import RPi.GPIO as GPIO

class CmdVelListener(Node): 
    def __init__(self):
        super().__init__('cmdvel_listener')
        self.subscription = self.create_subscription(
            Vector3,
            'cmdvel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        self.PWM = 15
        self.IN3 = 11
        self.IN4 = 13

        GPIO.setup(self.IN3, GPIO.OUT) # Connected to PWMA
        GPIO.setup(self.IN4, GPIO.OUT) # Connected to AIN2
        GPIO.setup(self.PWM, GPIO.OUT) # Connected to AIN1

        self.p = GPIO.PWM(self.PWM, 100)
        self.p.start(0)
              

    def listener_callback(self, msg:Vector3):
        self.p.ChangeDutyCycle(msg.z)
        GPIO.output(self.IN3, GPIO.HIGH) # Set AIN1
        GPIO.output(self.IN4, GPIO.LOW) # Set AIN2
        self.get_logger().info('I heard: "%s"' % msg.z)

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