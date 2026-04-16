turtlebot4_beep : make beep sound of turtlebot4
  - ros2 run turtlebot4_beep beep_node
  - ros2 launch turtlebot4_beep beep_launch.py

4. 빌드 및 환경 설정
cd ~/rokey_ws
colcon build colcon build --symlink-install --packages-select turtlebot4_beep
source install/setup.bash
ros2 run turtlebot4_beep beep_node

my_data.zip = 웹캠 카메라 이미지
capture.py = 웹캠 연결 시 s 키 누르면 파일 만들고 이미지 저장
  - 저장할 폴더 이름, 이미지 이름 바꾸기

makedir = 새로운 폴더 만들기
split = 이미지를 test, train, val 로 나누기
split_label = 라벨을 각 이미지 폴더에 맞게 라벨 결과를 나누기 

yolo_test = 이미지를 yolo에 학습시키는 파일이다 - **colab으로 돌려야 한다.**
  - test, train, valid 폴더로 나누어진 zip 파일 google drvie에 올린다.
  - 이후 순차적으로 돌리면 된다.
  - 돌릴 때 마다 파라미터를 수정해야 한다. 
  - 처음 각각 개별적으로 돌려보고 잘 된다면 원클릭 부분으로 돌리면 된다.

  - https://www.notion.so/x1anzhen/Team-5d0815523bb982439d6e010213e56127?source=copy_link
