


#### Introduction
Lidar technology uses near-infrared light to detect objects around a vehicle. We will see how sick scan lms 1xx will operate in ROS.

#### Prerequisites
1. Git clone the sick scan repository from the following link: 
      > https://github.com/SICKAG/sick_scan
2. Now from the terminal give the following commands
     > cd "workspace name" 
 
     > catkin_make
  
#### How to operate?
1. Connect the lidar to the laptop/PC using the M12-RJ45 connecting cabel.
     
    
![index](https://user-images.githubusercontent.com/99531399/156824522-17e690ea-39cd-4705-9b5a-ce5ecdc0677e.jpeg)


2. Go to settings-> Network. Add a new profile. 
3. In the **Identity** add a new name.


 ![Screenshot from 2022-03-05 00-27-57](https://user-images.githubusercontent.com/99531399/156825185-91945e52-33d7-4555-bcf7-41b75e269d21.png)


4. Select IPv4. Change the method to **Manual**. Fillup the address and netmask section.


![Screenshot from 2022-03-05 00-31-51](https://user-images.githubusercontent.com/99531399/156825656-839d346f-f670-4fed-9274-a8ce8a9166b5.png)




5. Click **Add**.
6. From the files open your workspace, in the workspace go to the src folder and open the launch folder.
7. The sick_lms_1xx.launch file has a arg tag, in the arg tag change the default IP address to the IP address of lidar. 
8. Now in the terminal launch the file using the following command: 
     
     >'roslaunch sick_scan sick_lms_1xx.launch'
8. In a new ternimal give the foloowing command simultaneously
      
      > rviz
9. In rviz change the fixed frame to **laser**
10. At the bottom of the rviz click on the **Add** option.
11. Add a new display: **PointCloud2**
12. Change the topic of PointCloud2 to **/cloud**

#### Output
After following the above steps you will see a point cloud in the rviz. The point cloud is a collection of points representing the objects around the lidar.  

