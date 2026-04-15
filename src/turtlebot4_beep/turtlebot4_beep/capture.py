import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

class AutoImageSaver(Node):
    def __init__(self):
        super().__init__('auto_image_saver')
        # 토픽 구독
        self.subscription = self.create_subscription(Image, '/image_raw', self.listener_callback, 10)
        self.bridge = CvBridge()
        
        # 폴더 설정
        self.folder_name = "webcamimage"
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)
            print(f"📂 폴더 생성됨: {self.folder_name}")
        
        # 1번부터 시작 (파일 이름용)
        self.img_count = 1
        self.current_frame = None

        # --- 핵심: 2초마다 실행되는 타이머 생성 ---
        # 2.0초마다 self.timer_callback 함수를 실행합니다.
        self.timer = self.create_timer(2.0, self.timer_callback)
        
        print("🚀 자동 저장 시작: 2초 간격으로 이미지를 저장합니다.")
        print("⌨️ 종료하려면 터미널에서 Ctrl+C 를 누르세요.")

    def listener_callback(self, data):
        # 실시간 프레임을 계속 업데이트
        self.current_frame = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        
        # 실시간 화면 확인용 (필요 없으면 주석 처리 가능)
        cv2.imshow("Webcam Auto Capture", self.current_frame)
        cv2.waitKey(1)

    def timer_callback(self):
        # 현재 카메라 프레임이 있는지 확인
        if self.current_frame is not None:
            file_name = f"webcamimage{self.img_count}.jpg"
            file_path = os.path.join(self.folder_name, file_name)
            
            # 이미지 저장
            cv2.imwrite(file_path, self.current_frame)
            
            print(f"📸 [자동저장] {file_name}")
            
            # 번호 증가
            self.img_count += 1
        else:
            print("⚠️ 아직 카메라 영상이 들어오지 않고 있습니다.")

def main(args=None):
    rclpy.init(args=args)
    node = AutoImageSaver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\n👋 사용자에 의해 중단되었습니다.")
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()