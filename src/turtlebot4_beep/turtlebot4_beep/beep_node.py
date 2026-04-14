import rclpy
from rclpy.node import Node
from irobot_create_msgs.msg import AudioNoteVector, AudioNote
from builtin_interfaces.msg import Duration


class BeepNode(Node):

    def __init__(self):
        super().__init__('beep_node')

        # parameter
        self.declare_parameter('robot_name', 'robot4')
        robot_name = self.get_parameter('robot_name').value

        topic_name = f'/{robot_name}/cmd_audio'

        self.get_logger().info(f'Publishing to {topic_name}')

        # ✅ REAL publisher (this was missing)
        self.publisher_ = self.create_publisher(
            AudioNoteVector,
            topic_name,
            10
        )

        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = AudioNoteVector()

        note = AudioNote()
        note.frequency = 1000   # sound pitch (Hz)
        note.max_runtime = Duration(sec=0, nanosec=200000000)  # 0.2 seconds

        msg.notes = [note]

        self.publisher_.publish(msg)

        self.get_logger().info('🔊 Beep sent')


def main(args=None):
    rclpy.init(args=args)
    node = BeepNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()