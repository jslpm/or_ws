import math
import rclpy

from rclpy.node import Node
from control_msgs.msg import MultiDOFCommand

class TrajectorySender(Node):
    
    def __init__(self):
        super().__init__("trajectory_sender")
        self.pub = self.create_publisher(MultiDOFCommand, "joint_pid_controller/reference", 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.traj_msg = MultiDOFCommand()
        self.traj_msg.dof_names = ["joint_1", "joint_2"]

    def timer_callback(self):
        time = self.get_clock().now().nanoseconds * 10e-10
        period = 10
        frequency = 1 / period
        omega = 2 * math.pi * frequency
        amplitude = math.pi / 2

        pos = amplitude * math.sin(omega * time)

        self.traj_msg.values = [pos - math.pi/2, pos]

        self.pub.publish(self.traj_msg)


def main():
    rclpy.init()
    node = TrajectorySender()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()