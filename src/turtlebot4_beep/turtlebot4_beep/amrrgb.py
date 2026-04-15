import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import threading
import tkinter as tk
from tkinter import Label, Button
from PIL import Image as PILImage, ImageTk


class ImageCaptureGUI(Node):
    def __init__(self):
        super().__init__('image_capture_gui')

        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.listener_callback,
            10
        )

        self.bridge = CvBridge()
        self.current_frame = None
        self.img_count = 1

        # 저장 폴더 이름
        self.folder_name = "amrrgb"
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)
            print(f"📂 폴더 생성됨: {self.folder_name}")

        # GUI 생성
        self.root = tk.Tk()
        self.root.title("AMR RGB Capture")

        self.image_label = Label(self.root)
        self.image_label.pack()

        self.capture_button = Button(
            self.root,
            text="캡처",
            command=self.capture_image,
            font=("Arial", 14),
            width=15,
            height=2
        )
        self.capture_button.pack(pady=10)

        self.status_label = Label(self.root, text="카메라 대기 중...", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.update_gui()

    def listener_callback(self, data):
        try:
            self.current_frame = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        except Exception as e:
            self.get_logger().error(f"이미지 변환 실패: {e}")

    def update_gui(self):
        if self.current_frame is not None:
            frame_rgb = cv2.cvtColor(self.current_frame, cv2.COLOR_BGR2RGB)
            pil_image = PILImage.fromarray(frame_rgb)
            pil_image = pil_image.resize((640, 480))
            tk_image = ImageTk.PhotoImage(image=pil_image)

            self.image_label.imgtk = tk_image
            self.image_label.configure(image=tk_image)
            self.status_label.config(text="실시간 영상 표시 중")
        else:
            self.status_label.config(text="카메라 영상 대기 중...")

        self.root.after(30, self.update_gui)

    def capture_image(self):
        if self.current_frame is not None:
            file_name = f"amrrgb{self.img_count}.jpg"
            file_path = os.path.join(self.folder_name, file_name)

            cv2.imwrite(file_path, self.current_frame)
            print(f"📸 저장됨: {file_path}")
            self.status_label.config(text=f"저장됨: {file_name}")

            self.img_count += 1
        else:
            print("⚠️ 저장할 영상이 아직 없습니다.")
            self.status_label.config(text="저장 실패: 카메라 영상 없음")

    def on_close(self):
        self.root.quit()
        self.root.destroy()

    def run_gui(self):
        self.root.mainloop()


def ros_spin(node):
    rclpy.spin(node)


def main(args=None):
    rclpy.init(args=args)
    node = ImageCaptureGUI()

    ros_thread = threading.Thread(target=ros_spin, args=(node,), daemon=True)
    ros_thread.start()

    try:
        node.run_gui()
    except KeyboardInterrupt:
        print("\n👋 사용자에 의해 종료되었습니다.")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
