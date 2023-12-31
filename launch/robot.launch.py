from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import AnyLaunchDescriptionSource, PythonLaunchDescriptionSource
import xacro
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_name = 'autonomous_robot'
    file_subpath = 'robot.urdf.xacro'

    xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
    robot_description_raw = xacro.process_file(xacro_file).toxml()
    
    node_robot_state_publisher = Node(
        name='robot_state_publisher',
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description_raw}]
    )

    robot_node = Node(
        package='autonomous_robot',
        executable='velocity_listener',
        name="robot_node",
        parameters=[{'use_sim_time': True}] 
    )
    
    joint_state_publisher_node = Node( # Not used
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        arguments=[xacro_file],
    )

    foxglove_bridge_share = get_package_share_directory("foxglove_bridge")

    foxglove_bridge_launch_file_path = os.path.join(
        foxglove_bridge_share, 'launch', 'foxglove_bridge_launch.xml'
    )

    foxglove_bridge_launch = IncludeLaunchDescription( # Not used
        AnyLaunchDescriptionSource(foxglove_bridge_launch_file_path)
    )

    return LaunchDescription([node_robot_state_publisher, robot_node])