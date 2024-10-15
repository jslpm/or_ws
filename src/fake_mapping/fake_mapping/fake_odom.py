import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry


class FakeOdomPublisher(Node):

    def __init__(self):
        super().__init__("fake_odom_publisher")
        self.get_logger().info("Publishing fake odom msg")
        self.pub = self.create_publisher(Odometry, "odom", 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.odometry_msg = Odometry()

    def timer_callback(self):
        self.odometry_msg.header.stamp = self.get_clock().now().to_msg()
        self.odometry_msg.header.frame_id = "world"

        self.odometry_msg.child_frame_id = "odom"

        self.pub.publish(self.odometry_msg)


def main():
    rclpy.init()
    node = FakeOdomPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
