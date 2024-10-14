import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    package_name = 'arm_robot_description'

    ld = LaunchDescription()

    # Get urdf description
    urdf_path = os.path.join(get_package_share_directory(package_name), 'urdf', 'arm_robot.urdf')
    urdf = open(urdf_path).read()

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[
            {'robot_description': urdf}
        ]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d' + os.path.join(get_package_share_directory(package_name), 'rviz', 'robot_description_config.rviz')],
    )


    ld.add_action(robot_state_publisher_node)
    ld.add_action(rviz_node)

    return ld
