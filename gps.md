# GPS-AtlasLink® GNSS Smart Antenna
## Introduction
   Global positioning system (GPS) is a network of satellites and receiving devices used to determine the location of something on Earth.

### Pre-requisites
 1. Place the antenna with an unobstructed view of the sky.
 
 2. **LED Display:** 
    
    AtlasLink uses a single LED that provides system information based on the color of the LED as follows: 
      
      • Blinking Red - Power on
      
      • Blinking Amber - GNSS position available, including RTK float and Atlas
      
      • Blinking Green - RTK-fixed or Atlas-converged position available
      
      • Blinking any color – Receiver operational
    
    **WARNING:** If at any time the LED turns to a solid color for an extended period of time, the receiver has malfunctioned
  
 3. Install the following ROS Package:
     
     ```bash
     sudo apt install ros-noetic-nmea-navsat-driver
     ``` 

### How to operate?
  1. Connect the GPS to the laptop/PC using the connecting cabel.

  2. In the first terminal Run the master node: 
     ```bash
     roscore 
     ``` 
  3. In the Second terminal give the following command: *To Check if Connection is solid*
     ```bash
     udevadm info -a -p  $(udevadm info -q path -n /dev/ttyUSB0) 
     ```
     Next
     ```bash
     sudo chmod 777 /dev/ttyUSB0 
     rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyUSB0 _baud:=9600 
     ```
  4. In a new terminal run the following command:
     ```bash 
     rostopic echo /fix
     ```
### Output
After following above steps you will get the location in the terminal.
    
     
