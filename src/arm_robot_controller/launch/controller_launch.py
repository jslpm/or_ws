import os

from ament_index_python import get_package_share_path
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue


def generate_launch_description():

    package_name = "arm_robot_controller"

    robot_controllers_config = get_package_share_path(package_name) / "config" / "arm_robot_controller.yaml"

    controller_config_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[str(robot_controllers_config)],
        output="screen"
    )

    joint_state_broadcaster_node = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        output="screen",
    )

    joint_trajectory_controller_node = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_pid_controller"],
        output="screen",
    )
    

    # Add actions and return Launch Description
    return LaunchDescription([
        controller_config_node,
        joint_state_broadcaster_node,
        joint_trajectory_controller_node,
    ])
