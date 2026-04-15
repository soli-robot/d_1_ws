turtlebot4_beep : make beep sound of turtlebot4
  - ros2 run turtlebot4_beep beep_node
  - ros2 launch turtlebot4_beep beep_launch.py

4. 빌드 및 환경 설정
cd ~/rokey_ws
colcon build colcon build --symlink-install --packages-select turtlebot4_beep
source install/setup.bash
ros2 run turtlebot4_beep beep_node
