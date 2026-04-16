import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

class ManualImageSaver(Node):
    def __init__(self):
        super().__init__('manual_image_saver')
        # 토픽 구독 (USB 웹캠)
        self.subscription = self.create_subscription(Image, '/image_raw', self.listener_callback, 10)
        self.bridge = CvBridge()
        
        # 저장할 폴더 설정
        self.folder_name = "webcamimage_mix"
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)
            print(f"📂 폴더 생성됨: {self.folder_name}")
        
        # 파일 번호 초기화 (1번부터 시작)
        self.img_count = 1
        self.current_frame = None
        
        print("🚀 수동 캡처 모드가 준비되었습니다.")
        print("⌨️ 영상 창을 클릭한 후 's' 키를 누르면 사진이 저장됩니다.")
        print("⌨️ 종료하려면 'q' 키를 누르세요.")

    def listener_callback(self, data):
        # ROS 이미지를 OpenCV 형식으로 변환
        self.current_frame = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        
        # 실시간 화면 표시
        cv2.imshow("Webcam Capture View", self.current_frame)
        
        # 키 입력 대기 (1ms)
        key = cv2.waitKey(1) & 0xFF
        
        # 's' 키를 눌렀을 때 저장 로직
        if key == ord('s'):
            if self.current_frame is not None:
                # 파일 이름 결정: webcamimage1.jpg, webcamimage2.jpg ...
                file_name = f"webcamimage_mix{self.img_count}.jpg"
                file_path = os.path.join(self.folder_name, file_name)
                
                # 이미지 저장
                cv2.imwrite(file_path, self.current_frame)
                
                print(f"📸 [저장 완료] {file_path}")
                
                # 다음 저장을 위해 번호 1 증가
                self.img_count += 1
            else:
                print("⚠️ 저장할 영상 프레임이 없습니다.")

        # 'q' 키를 누르면 종료
        elif key == ord('q'):
            print("👋 프로그램을 종료합니다.")
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = ManualImageSaver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()