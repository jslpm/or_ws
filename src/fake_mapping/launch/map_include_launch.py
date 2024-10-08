
import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.launch_description_sources import AnyLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    package_name = 'fake_mapping'

    ld = LaunchDescription()

    # Include ydlidar launch
    launch1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ydlidar'), 'launch/ydlidar_launch.py')
        )
    )

    # Include slam_toolbox launch
    # launch2 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join(get_package_share_directory('slam_toolbox'), 'launch/online_sync_launch.py')
    #     )
    # )

    # Fake Odometry messsage node
    node1 = Node(
            package='fake_mapping',
            executable='fake_odom',
            name='fake_odom',
            output='screen',
            emulate_tty=True,
    )

    # Fake tf base to base_footprint broadcaster node
    node2 = Node(
            package='fake_mapping',
            executable='fake_tf_base_footprint',
            name='fake_tf_base_to_base_footprint',
            output='screen',
            emulate_tty=True,
    )

    # Fake tf odom to base_link broadcaster node 
    node3 = Node(
            package='fake_mapping',
            executable='fake_tf_odom',
            name='fake_tf_odom_to_base_link',
            output='screen',
            emulate_tty=True,
    )

    # rqt_graph node
    node4 = Node(
            package='rqt_graph',
            executable='rqt_graph',
            name='rqt_graph',
            output='screen',
            emulate_tty=True,
    )

    # slam_toolbox node
    node5 = Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            emulate_tty=True,
            arguments=['-d' + os.path.join(get_package_share_directory(package_name), 'rviz', 'laser_tf_map_config.rviz')]
    )

    

    ld.add_action(node1)
    ld.add_action(node2)
    ld.add_action(node3)
    ld.add_action(node4)
    ld.add_action(node5)

    ld.add_action(launch1)
    # ld.add_action(launch2)

    return ld

