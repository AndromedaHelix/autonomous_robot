from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'autonomous_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        # Add the xacro files to be included in the installation
        (os.path.join('share', package_name), ['description/robot.urdf.xacro']),
        (os.path.join('share', package_name), ['description/robot_include.xacro']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andromeda',
    maintainer_email='58833781+AndromedaHelix@users.noreply.github.com',
    description='Autonomous Holonomic Robot',
    license='Apache License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'velocity_listener = autonomous_robot.robot_cmdvel:main',
        ],
    },
)
