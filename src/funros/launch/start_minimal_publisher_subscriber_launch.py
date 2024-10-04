
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='funros',
            executable='minimal_publisher',
            name='my_publisher',
            output='screen',
            remappings=[
                ('topic', 'counter'),
            ]
        ),
        Node(
            package='funros',
            executable='minimal_subscriber',
            name='my_subscriber',
            output='screen',
            emulate_tty=True,
            remappings=[
                ('topic', 'counter'),
            ]
        ),
        Node(
            package='rqt_graph',
            executable='rqt_graph',
        )
    ])
