import rclpy
from rclpy.node import Node
import time
from demo_interface_pkg.msg import DemoTopicMsg

class CustomTopicPublisherNode(Node):

    def __init__(self):
        super().__init__('custom_topic_publisher_node')

        self.simple_msg_publisher = self.create_publisher(DemoTopicMsg, '/custom_msg_topic', 10)
        self.create_timer(2, self.timer_callback)

        self.get_logger().info('custom_topic_publisher_node初始化完成')

    def timer_callback(self):
        msg = DemoTopicMsg()
        msg.name = 'hello'
        msg.status = True
        msg.value = time.time()
        self.simple_msg_publisher.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)

    # 实例化节点
    demo_node = CustomTopicPublisherNode()
    try:
        rclpy.spin(demo_node)
    except KeyboardInterrupt:
        pass

    # 关闭节点，清理资源
    demo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()