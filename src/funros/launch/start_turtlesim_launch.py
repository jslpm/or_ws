
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle',
        ),
        Node(
            package='rqt_graph',
            executable='rqt_graph',
)
    ])