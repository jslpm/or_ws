import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    package_name = 'funros'
    ld = LaunchDescription()

    tf_broadcaster_node = Node(
        package="funros",
        executable="tf_broadcaster",
    )

    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim',
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d' + os.path.join(get_package_share_directory(package_name), 'rviz', 'turtle_tf.rviz')],
    )

    ld.add_action(tf_broadcaster_node)
    ld.add_action(turtlesim_node)
    ld.add_action(rviz_node)

    return ld
