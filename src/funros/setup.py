import os
from setuptools import find_packages, setup
from glob import glob

package_name = 'funros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*_launch.py')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.sdf')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jl-dimec',
    maintainer_email='jose.pascal@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "hello = funros.hello_ros:main",
            "minimal_publisher = funros.minimal_publisher:main",
            "minimal_subscriber = funros.minimal_subscriber:main",
            "time_publisher = funros.time_publisher:main",
            "example_service_server = funros.example_service_server:main",
            "example_service_client = funros.example_service_client:main",
            "tf_broadcaster = funros.tf_broadcaster:main",
        ],
    },
)
