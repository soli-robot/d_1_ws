from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot4_beep',
            executable='beep_node',
            name='beep_node',
            output='screen',
            parameters=[
                {'robot_name': 'robot4'}  # 필요하면 수정
            ]
        )
    ])