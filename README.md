# TDR-SDC Formula Student Driverless Simulator
[![ROS Build](https://github.com/TDR-SDC/fsd_simulator/actions/workflows/test_build.yml/badge.svg?branch=master)](https://github.com/TDR-SDC/fsd_simulator/actions/workflows/test_build.yml)
### Welcome to the official simulation codebase of TDR-SDC for Formula Student Driverless

## Packages
1. `eufs_description`: contains the urdf of the model
2. `eufs_gazebo`: contains all the gazebo worlds and simulation requirements
3. `robot_control`: contains nodes to actuate the model in simulation
4. `gmapping`: openSLAM-gmapping package
5. `pure_pursuit`: Lateral controller

## Installation
### Prerequisites
- Ubuntu 20.04
- Cuda 11.0
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda-repo-ubuntu2004-11-0-local_11.0.2-450.51.05-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2004-11-0-local_11.0.2-450.51.05-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu2004-11-0-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda-11-0
```
Add following commands in .bashrc
```bash
export PATH=/usr/local/cuda-11.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64\
                         ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
- CUDNN 8.0.5 
 
  Install the cudnn 8.0.5 from the official website 
    
![cudnn](https://user-images.githubusercontent.com/99531399/227703445-35a36155-f8a0-47b4-a4fc-5b7f0d956728.png)

After installation, open the terminal and extract the file using the following commands:
```bash
cd Downloads
tar -zxf <copy the file name>.tgz

```
A folder named cuda will be built, transfer it to home, the execute the following commands:

```bash
  cd cuda/
  sudo cp lib64/* /usr/local/cuda/lib64/
  sudo cp include/* /usr/local/cuda/include/
  sudo reboot 
```
After reboot to check if the cudnn has been installled correctly, give th following command:
```bash 
dpkg -l libcudnn8
```

- OpenCV4 4.5.5 from source
- Darknet (https://github.com/AlexeyAB/darknet)
- Install [ros-noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)
- cmake minimum version 3.19.0 (https://answers.ros.org/question/293119/how-can-i-updateremove-cmake-without-partially-deleting-my-ros-distribution/)

   ![cmake](https://user-images.githubusercontent.com/99531399/227709016-9fabed4f-eb7e-4745-8a11-b1a81d990f75.png)
   
  To check the cmake version give the following command:
  ```bash
  cmake --version
  ```


- libfreenect (https://github.com/OpenKinect/libfreenect.git) see libfreenect.md (In addition to the instructions given in the repository, see the command below)
```bash
sudo apt-get install freenect
```
- Python Packages:
  - pcl
  - scipy 
```bash
sudo apt install python3-pcl
sudo apt install python3-scipy
```
-  ROS Packages:
    - ros-noetic-ackermann-msgs
    - ros-noetic-twist-mux
    - ros-noetic-joy
    - ros-noetic-controller-manager
    - ros-noetic-robotnik-msgs
    - ros-noetic-velodyne-simulator
    - ros-noetic-effort-controllers
    - ros-noetic-velocity-controllers
    - ros-noetic-joint-state-controller
    - ros-noetic-gazebo-ros-control
    - ros-noetic-navigation
    - ros-noetic-gmapping
    - ros-noetic-rgbd-launch
    - ros-noetic-nmea-navsat-driver
    - ros-noetic-ros-numpy

Here's a direct terminal command to install all of them at once:
```bash
sudo apt install ros-noetic-ackermann-msgs ros-noetic-twist-mux ros-noetic-joy ros-noetic-controller-manager ros-noetic-velodyne-simulator ros-noetic-effort-controllers ros-noetic-velocity-controllers ros-noetic-joint-state-controller ros-noetic-gazebo-ros-control ros-noetic-navigation ros-noetic-gmapping ros-noetic-rgbd-launch ros-noetic-nmea-navsat-driver ros-noetic-ros-numpy
```

### How to build
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/TDR-SDC/fsd_simulator
cd ..
catkin_make
```

## Running the simulation
1. Source the workspace:

- ```source ~/catkin_ws/devel/setup.bash```

2. Enter the three given commands in different terminals after using the sourcing the workspace
```bash
roslaunch eufs_gazebo small_track.launch                 # launch eufs simulator
roslaunch gmapping gmapping.launch                       # launch gmapping
roslaunch pure_pursuit pure_pursuit.launch               # launch pure_pursuit controller
roslaunch perception_pipeline perception_pipeline.launch # launch perception YOLOv4 tiny pipeline
roslaunch eufs_gazebo sensor_integration.launch          # launch integrated pipeline
```
3. To Launch Complete Pipeline in Simulator:
```bash
roslaunch eufs_gazebo sensor_integration.launch                 # launch Complete Pipeline
``` 
4. To Launch Complete Pipeline Physically:
```bash
roslaunch eufs_gazebo complete_pipeline.launch                 # launch Complete Pipeline
``` 
