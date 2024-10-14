# gazebo_empty_launch.py
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    # Declare arguments for the world file and other configurations
    world_file = LaunchConfiguration('world')

    return LaunchDescription([
        # Declare the path to the world file
        DeclareLaunchArgument(
            'world',
            default_value='worlds/empty.world',  # Replace with your custom world file if necessary
            description='World file to load'),

        # Launch Gazebo Classic server
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_file],
            output='screen'
        ),

        # Launch Gazebo client
        # ExecuteProcess(
        #     cmd=['gzclient'],
        #     output='screen'
        # ),
    ])
