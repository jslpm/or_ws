import rclpy
import math
from rclpy.node import Node

from std_msgs.msg import Float64


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Float64, 'topic', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = Float64()
        time = self.get_clock().now().to_msg()
        # time = self.get_clock().now().nanoseconds * 10e-10
        # msg.data = math.sin(2 * math.pi * time / 10)
        self.publisher_.publish(msg)
        
        self.get_logger().info(f'Publishing: {time}')


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
