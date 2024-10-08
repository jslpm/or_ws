
import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    package_name = "fake_mapping"

    return LaunchDescription([
        # Fake Odometry messsage node
        Node(
            package='fake_mapping',
            executable='fake_odom',
            name='fake_odom',
            output='screen',
        ),
        # Fake tf base to base_footprint broadcaster node
        Node(
            package='fake_mapping',
            executable='fake_tf_base_footprint',
            name='fake_tf_base_to_base_footprint',
            output='screen',
        ),
        # Fake tf odomo to base_link broadcaster node 
        Node(
            package='fake_mapping',
            executable='fake_tf_odom',
            name='fake_tf_odom_to_base_link',
            output='screen',
        ),
        # rqt_graph node
        Node(
            package='rqt_graph',
            executable='rqt_graph',
            name='rqt_graph',
            output='screen',
        ),
        # slam_toolbox node
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d' + os.path.join(get_package_share_directory(package_name), 'rviz', 'laser_tf_map_config.rviz')]
        )
    ])
