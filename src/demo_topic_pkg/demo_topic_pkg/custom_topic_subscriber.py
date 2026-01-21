import rclpy
from rclpy.node import Node

from demo_interface_pkg.msg import DemoTopicMsg

class CustomTopicSubscriberNode(Node):

    def __init__(self):
        super().__init__('custom_topic_subscriber_node')

        self.simple_msg_subscriber = self.create_subscription(
            DemoTopicMsg, 
            '/custom_msg_topic', 
            self.simple_msg_callback,
            10
        )

        self.get_logger().info('custom_topic_subscriber_node初始化完成')

    def simple_msg_callback(self, msg: DemoTopicMsg):
        self.get_logger().info(f'receive custom msg, content name: {msg.name}, status: {msg.status}, value: {msg.value}')

def main(args=None):
    rclpy.init(args=args)

    # 实例化节点
    demo_node = CustomTopicSubscriberNode()
    try:
        rclpy.spin(demo_node)
    except KeyboardInterrupt:
        pass

    # 关闭节点，清理资源
    demo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()