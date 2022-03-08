# Sick lms 111


## Introduction
Lidar technology uses near-infrared light to detect objects around a vehicle. We will see how sick scan lms 111 will operate in ROS.


 ![Screenshot from 2022-03-05 11-59-21](https://user-images.githubusercontent.com/99531399/156871449-1f6674ad-a2cc-407e-a4d4-8b780c620060.png)




### Prerequisites
1. Git clone the sick scan repository from the following link: 
      > https://github.com/SICKAG/sick_scan
2. Now from the terminal give the following commands
     > cd < workspace name > 
 
     > catkin_make
  
### How to operate?
1. Connect the lidar to the laptop/PC using the M12-RJ45 connecting cabel.
     
    
![index](https://user-images.githubusercontent.com/99531399/156824522-17e690ea-39cd-4705-9b5a-ce5ecdc0677e.jpeg)


2. Go to settings-> Network. Add a new profile. 
3. In the **Identity** add a new name.


![Screenshot from 2022-03-05 11-47-07](https://user-images.githubusercontent.com/99531399/156871078-4646a48a-a7b0-45c7-94fa-9ae98189b5ca.png)



4. Select IPv4. Change the method to **Manual**. Fillup the address and netmask section.


![Screenshot from 2022-03-05 12-31-57](https://user-images.githubusercontent.com/99531399/156872643-4d218510-1460-4672-ad0b-2ddc8f21904a.png)





5. Click **Apply**.
6. From the files open your workspace, in the workspace go to the src folder and open the launch folder.
7. The sick_lms_1xx.launch file has a arg tag, in the arg tag change the default IP address to the IP address of lidar i.e **169.254.195.208**. 
8. Now in the terminal launch the file using the following command: 
     
     > roslaunch sick_scan sick_lms_1xx.launch
8. In a new ternimal give the following command simultaneously.
      
      > rviz
9. In rviz change the fixed frame to **laser**
10. At the bottom of the rviz click on the **Add** option.
11. Add a new display: **PointCloud2**
12. Change the topic of PointCloud2 to **/cloud**

### Output
After following the above steps you will see a point cloud in the rviz. A point cloud is a collection of points representing the objects around the lidar.  

