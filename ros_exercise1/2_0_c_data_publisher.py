import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DataPublisher(Node):
    def __init__(self):
        super().__init__('data_publisher')
        self.pub = self.create_publisher(String, 'data_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        msg = String()
        msg.data = "Hello ROS2"
        self.pub.publish(msg)
        self.get_logger().info(msg.data)

def main():
    rclpy.init()
    node = DataPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
