from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # 声明 launch 参数
    declared_arguments = [
        DeclareLaunchArgument(
            'content_prefix',
            default_value='Hello World',
            description='内容前缀'
        ),
    ]

    # 发布节点
    publisher_node = Node(
        package='demo_topic_pkg',
        executable='simple_topic_publisher_parameterized',
        name='topic_publisher',
        output='both',
        parameters=[
            {"content_prefix": LaunchConfiguration('content_prefix')},
        ]
    )

    # 接收
    subscriber_node = Node(
        package='demo_topic_pkg',
        executable='simple_topic_subscriber',
        name='topic_subscriber',
        output='both',
    )

    return LaunchDescription(
        declared_arguments +
        [
            publisher_node,
            subscriber_node
        ]
    )
