from sensor_msgs.msg import Image
import rclpy
from rclpy.node import Node

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.pub = self.create_publisher(Image, 'image_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_image)

    def publish_image(self):
        msg = Image()
        msg.height = 0
        msg.width = 0
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = ImagePublisher()
    rclpy.spin(node)
    rclpy.shutdown()
