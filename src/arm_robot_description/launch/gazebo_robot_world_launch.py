# gazebo_custom_world_launch.py

import os

from ament_index_python import get_package_share_path
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue


def generate_launch_description():

    # Package name
    package_name = 'arm_robot_description'

    # Create launch description object
    ld = LaunchDescription()

    # Get urdf description
    xacro_path = os.path.join(get_package_share_directory(package_name), 'urdf', 'arm_robot.xacro')
    
    # Declare arguments for the world file and other configurations
    package_path = get_package_share_path('arm_robot_description')
    world_path = package_path / 'worlds' / 'numbers.world'
    world_file = LaunchConfiguration('world')

    world_launch_arg = DeclareLaunchArgument(
        'world',
        default_value=str(world_path),  # Replace with your custom world file if necessary
        description='World file to load'
    )
    
    gazebo_process = ExecuteProcess(
        cmd=['gazebo', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', '--verbose', world_file],
        output='screen'
    )

    # Create robot_state_publisher node with xacro file
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{
            'robot_description': ParameterValue(Command(['xacro ', str(xacro_path)]), value_type=str)
        }],
    )

    # Spawn robot
    spawn_robot_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=['-topic', 'robot_description','-entity', 'arm_robot',"-x", "0.0", "-y", "0.0", "-z", "0.0", "-R", "0.0", "-P", "0.0", "-Y", "1.5707"]
    )

    # Add actions and return Launch Description
    return LaunchDescription([
        world_launch_arg,
        robot_state_publisher_node,
        gazebo_process,
        spawn_robot_node,
        
    ])
