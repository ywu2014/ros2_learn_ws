import rclpy
from rclpy.node import Node

# 定义一个类, 需要继成基类Node
class DemoNode(Node):

    def __init__(self):
        # 给节点命名
        super().__init__('demo_node')

        self.get_logger().info('demo_node初始化完成')

        self.func1()

    def func1(self):
        """
        实现xxx功能
        """
        self.get_logger().info('功能1实现...')

# 主函数：程序的入口
def main(args=None):
    rclpy.init(args=args) # 初始化 ROS2 环境

    # 实例化节点
    demo_node = DemoNode()
    try:
        rclpy.spin(demo_node) # 阻塞程序,直到手动停止
    except KeyboardInterrupt:
        pass

    # 关闭节点，清理资源
    demo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()