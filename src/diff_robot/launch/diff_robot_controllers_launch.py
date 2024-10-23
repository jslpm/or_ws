import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess


def generate_launch_description():

    # Create launch description object
    ld = LaunchDescription()

    # start joint_state_broadcaster controller
    joint_state_broadcaster_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set', 'active', 'joint_state_broadcaster'],
        output='screen'
    )

    # start diff_drive controller
    diff_drive_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set', 'active', 'diff_drive_controller'],
        output='screen'
    )

    # Add nodes to launch description
    ld.add_action(joint_state_broadcaster_controller)
    ld.add_action(diff_drive_controller)


    return ld
