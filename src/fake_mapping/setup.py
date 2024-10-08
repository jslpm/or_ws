import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'fake_mapping'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*_launch.py')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*_config.rviz')),
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
            "fake_tf_odom=fake_mapping.fake_tf_broadcaster:main",
            "fake_odom=fake_mapping.fake_odom:main",
            "fake_tf_base_footprint=fake_mapping.fake_tf_base_footprint:main",
        ],
    },
)
