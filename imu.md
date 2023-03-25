# IMU - AHRS8


## Introduction
An Inertial Measurement Unit (IMU) is a device that can measure and report specific gravity and angular rate of an object to which it is attached. An IMU typically consists of: Gyroscopes: providing a measure angular rate. Accelerometers: providing a measure specific force/acceleration.
  
### How to operate?
1. Connect the IMU to the laptop/PC using the connecting cabel.
2. In the first terminal give the following commands:
    ######To Check if Connection is solid
    ```bash
      udevadm info -a -p  $(udevadm info -q path -n /dev/ttyUSB0)
     ```
    Next
    ```bash
      sudo chmod 777 /dev/ttyUSB0
     ```

3. Then run the following commands:
     ```bash
     source ~/< workspace name>/devel/setup.bash
     cd < workspace_name >
     catkin_make
     roslaunch sparton_ahrs8_driver ahrs-8.launch
     ```

4.  In the Second terminal give the following command:
      ```bash
      rviz
      ```
5. At the bottom of the rviz click on the **Add** option.
6. Now click on **By Topic** and add a new display: **imu** 
7. In rviz change the fixed frame to **fcu**

### Output
After following the above steps you will see a arrow in rviz.

