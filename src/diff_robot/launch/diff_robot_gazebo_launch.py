import os

from ament_index_python import get_package_share_directory
from ament_index_python import get_package_share_path
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import Command
from launch.substitutions import LaunchConfiguration
from launch_ros.descriptions import ParameterValue
from launch_ros.actions import Node


def generate_launch_description():

    # Package name
    package_name = 'diff_robot'

    # Package path
    package_path = get_package_share_path(package_name)

    # Declare arguments for the world
    world_path = package_path / 'worlds' / 'empty.world'
    world_file = LaunchConfiguration('world')

    world_launch_arg = DeclareLaunchArgument(
        'world',
        default_value=str(world_path),  # Replace with your custom world file if necessary
        description='World file to load'
    )

    # Create launch description object
    ld = LaunchDescription()

    # Get urdf description
    xacro_path = os.path.join(get_package_share_directory(package_name), 'urdf', 'diff_robot.xacro')

    # Create robot_state_publisher node with xacro file
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{
            'robot_description': ParameterValue(Command(['xacro ', str(xacro_path)]), value_type=str)
        }],
    )

    # Create joint_state_publisher_gui node
    # joint_state_publisher_gui_node = Node(
    #     package='joint_state_publisher_gui',
    #     executable='joint_state_publisher_gui',
    #     name='joint_state_publisher_gui',
    #     output='screen',
    # )

    # Create joint_state_publisher node
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{'use_sim_time' : True}],
    )

    # Create rviz node with custom config file
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d' + os.path.join(get_package_share_directory(package_name), 'rviz', 'model_robot_config.rviz')],
    )

    # Start gazebo with custom world
    gazebo_process = ExecuteProcess(
        cmd=['gazebo', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', '--verbose', world_file],
        output='screen'
    )

    # Spawn robot
    spawn_robot_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=['-topic', 'robot_description','-entity', 'diff_robot',"-x", "0.0", "-y", "0.0", "-z", "0.0", "-R", "0.0", "-P", "0.0", "-Y", "0.0"]
    )

    # Add nodes to launch description
    ld.add_action(robot_state_publisher_node)
    ld.add_action(rviz_node)
    ld.add_action(joint_state_publisher_node)
    ld.add_action(world_launch_arg)
    ld.add_action(gazebo_process)
    ld.add_action(spawn_robot_node)

    return ld
