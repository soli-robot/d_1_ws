from sensor_msgs.msg import Image
import rclpy
from rclpy.node import Node

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.sub = self.create_subscription(
            Image,
            'image_topic',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info("이미지 받음")

def main():
    rclpy.init()
    node = ImageSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
