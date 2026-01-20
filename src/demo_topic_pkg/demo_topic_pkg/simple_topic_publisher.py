import rclpy
from rclpy.node import Node
import time

from std_msgs.msg import String

class SimpleTopicPublisherNode(Node):

    def __init__(self):
        super().__init__('simple_topic_publisher_node')

        self.simple_msg_publisher = self.create_publisher(String, '/simple_msg_topic', 10)
        self.create_timer(2, self.timer_callback)

        self.get_logger().info('simple_topic_publisher_node初始化完成')

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, ROS2 {time.time()}'
        self.simple_msg_publisher.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)

    # 实例化节点
    demo_node = SimpleTopicPublisherNode()
    try:
        rclpy.spin(demo_node)
    except KeyboardInterrupt:
        pass

    # 关闭节点，清理资源
    demo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()