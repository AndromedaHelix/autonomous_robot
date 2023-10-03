from setuptools import find_packages, setup

package_name = 'autonomous_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
                'robot = autonomous_robot.robot_cmdvel:main',
        ],
    },
)
