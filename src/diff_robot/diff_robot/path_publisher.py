import rclpy

from rclpy.node import Node
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

class PathPublisher(Node):

    def __init__(self):
        super().__init__("path_publisher")
        self.sub_to_odom = self.create_subscription(Odometry, 'diff_drive_controller/odom', self.sub_callback, 10)
        self.pub_path = self.create_publisher(Path, 'path', 10)
        self.path = Path()

    def sub_callback(self, data: Odometry):
        # Pose from odometry
        pose = PoseStamped()
        pose.header = data.header
        pose.pose = data.pose.pose

        # Populate path
        self.path.header = data.header
        self.path.poses.append(pose)

        # Publish path
        self.pub_path.publish(self.path)


def main():
    rclpy.init()
    node = PathPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()