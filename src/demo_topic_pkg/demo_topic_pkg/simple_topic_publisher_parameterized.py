import rclpy
from rclpy.node import Node
import time

from std_msgs.msg import String

class SimpleTopicPublisherParameterizdNode(Node):

    def __init__(self):
        super().__init__('simple_topic_publisher_parameterized_node')

        # 声明参数
        self.declare_parameter('content_prefix', 'Hello, ROS2')
        # 获取参数
        self.content_prefix = self.get_parameter('content_prefix').value

        self.simple_msg_publisher = self.create_publisher(String, '/simple_msg_topic', 10)
        self.create_timer(2, self.timer_callback)

        self.get_logger().info('simple_topic_publisher_node初始化完成')

    def timer_callback(self):
        msg = String()
        msg.data = f'{self.content_prefix} {time.time()}'
        self.simple_msg_publisher.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)

    # 实例化节点
    demo_node = SimpleTopicPublisherParameterizdNode()
    try:
        rclpy.spin(demo_node)
    except KeyboardInterrupt:
        pass

    # 关闭节点，清理资源
    demo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()