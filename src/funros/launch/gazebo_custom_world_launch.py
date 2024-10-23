# gazebo_custom_world_launch.py

from ament_index_python import get_package_share_path
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    
    # Declare arguments for the world file and other configurations
    package_path = get_package_share_path('funros')
    world_path = package_path / 'worlds' / 'numbers.world'
    world_file = LaunchConfiguration('world')

    return LaunchDescription([
        # Declare the path to the world file
        DeclareLaunchArgument(
            'world',
            default_value=str(world_path),  # Replace with your custom world file if necessary
            description='World file to load'
        ),

        # Launch Gazebo Classic server
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_file],
            output='screen'
        ),
    ])
