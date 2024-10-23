import os

from ament_index_python import get_package_share_directory
from ament_index_python import get_package_share_path
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import Command
from launch_ros.descriptions import ParameterValue
from launch_ros.actions import Node


def generate_launch_description():

    # Package name
    package_name = 'omni_robot'

    # Package path
    package_path = get_package_share_path(package_name)

    # Create launch description object
    ld = LaunchDescription()

    # Get urdf description
    xacro_path = os.path.join(get_package_share_directory(package_name), 'urdf', 'test_planar_plugin.xacro')

    # Create robot_state_publisher node with xacro file
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{
            'robot_description': ParameterValue(Command(['xacro ', str(xacro_path)]), value_type=str)
        }],
    )

    # Create joint_state_publisher node
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{'use_sim_time' : True}],
    )

    # Start gazebo with custom world
    gazebo_process = ExecuteProcess(
        cmd=['gazebo', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', '--verbose'],
        output='screen'
    )

    # Spawn robot
    spawn_robot_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=['-topic', 'robot_description','-entity', 'test_model',"-x", "0.0", "-y", "0.0", "-z", "0.0", "-R", "0.0", "-P", "0.0", "-Y", "0.0"]
    )

    # Add nodes to launch description
    ld.add_action(robot_state_publisher_node)
    ld.add_action(joint_state_publisher_node)
    ld.add_action(gazebo_process)
    ld.add_action(spawn_robot_node)

    return ld
