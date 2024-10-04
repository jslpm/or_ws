import rclpy
from rclpy.node import Node

class MyNode(Node): # Change SimpleNode

    def __init__(self):
        super().__init__("my_node") # Change simple_node
        self.get_logger().info("Hello ROS in Open Robotics course!")


def main(args=None):
    rclpy.init(args=args)
    my_node = MyNode() # Change simple_node
    rclpy.spin(my_node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
