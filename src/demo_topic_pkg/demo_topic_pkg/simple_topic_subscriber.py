import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class SimpleTopicSubscriberNode(Node):

    def __init__(self):
        super().__init__('simple_topic_subscriber_node')

        self.simple_msg_subscriber = self.create_subscription(
            String, 
            '/simple_msg_topic', 
            self.simple_msg_callback,
            10
        )

        self.get_logger().info('simple_topic_subscriber_node初始化完成')

    def simple_msg_callback(self, msg: String):
        self.get_logger().info(f'receive simple msg, content: {msg.data}')
        
def main(args=None):
    rclpy.init(args=args)

    # 实例化节点
    demo_node = SimpleTopicSubscriberNode()
    try:
        rclpy.spin(demo_node)
    except KeyboardInterrupt:
        pass

    # 关闭节点，清理资源
    demo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()