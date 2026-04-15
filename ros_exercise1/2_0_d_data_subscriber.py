import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DataSubscriber(Node):
    def __init__(self):
        super().__init__('data_subscriber')
        self.sub = self.create_subscription(
            String,
            'data_topic',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f"받음: {msg.data}")
        

def main():
    rclpy.init()
    node = DataSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
