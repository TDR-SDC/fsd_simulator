Introduction
Lidar technology uses near-infrared light to detect objects around a vehicle. We will see how sick scan lms 1xx will operate in ROS.

Supported Hardware
Install the lms1xx package in ubuntu using the following command in terminal: 'sudo apt-get install ros-noetic-lms1xx'

How to operate?
1. Connect the lidar to the laptop/PC using the M12-RJ45 connecting cabel.
(https://user-images.githubusercontent.com/99531399/156606072-82020a41-68b6-4996-a8ea-4da9c34c9e0c.png)
2. Go to settings-> Network. Add a new profile. 
3. Add the name. Select IPv4. Change the method to manual. Fill the address and netmask section.
4. Click Add.
5. From the files open your workspace in the src folder open the launch folder.
6. In the sick_lms_1xx.launch file change the default IP address.
7. Now in the terminal launch the file using the following command: 'roslaunch sick_scan sck_lms_1xx.launch'
8. In a new ternimal give the command 'rviz' simultaneously
