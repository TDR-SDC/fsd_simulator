# IMU - AHRS8


## Introduction
An Inertial Measurement Unit (IMU) is a device that can measure and report specific gravity and angular rate of an object to which it is attached. An IMU typically consists of: Gyroscopes: providing a measure angular rate. Accelerometers: providing a measure specific force/acceleration.

### Prerequisites
1. Git clone the IMU repository from the following link: 
      > 
2. Now from the terminal give the following commands
     > cd < workspace name > 
 
     > catkin_make
  
### How to operate?
1. Connect the IMU to the laptop/PC using the connecting cabel.
2. Open 3 terminals. In the first terminal give the following commands:
    > udevadm info -a -p  $(udevadm info -q path -n /dev/ttyUSB0)

    >  sudo chmod 777 /dev/ttyUSB0


3. In the second terminal give the following commands:
     > source ~/< workspace name>/devel/setup.bash
     > cd < workspace_name >
     > catkin_make
     >  roslaunch sparton_ahrs8_driver ahrs-8.launch

4.  In the third terminal give the following command:
      
      > rviz

5. At the bottom of the rviz click on the **Add** option.
6. Now click on **By Topic** and add a new display: **imu** 
7. In rviz change the fixed frame to **fcu**

### Output
After following the above steps you will see a arrow in rviz.

