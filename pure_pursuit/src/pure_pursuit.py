#! /usr/bin/env python3
import math
import numpy as np
import rospy
from nav_msgs.msg import *
from geometry_msgs.msg import *
import message_filters
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDriveStamped
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import tf
from std_msgs.msg import Float64MultiArray

global steer_list
steer_list=[]

car_len=0.3302   #meters
look_ahead = 3   #meters

pub2 = rospy.Publisher('/point',PointStamped,queue_size=1)   #publisher for a pointstamped topic to visualize lookahead point in rviz 

print("pure_pursuit controller started ")


# function to get the steering value for a given lookahead distance 
def get_steering(goal_y):
    steer= math.atan((2*goal_y*car_len)/(look_ahead**2))
    
    if steer > 50*np.pi/180:
        steer = 50*np.pi/180
    if steer < -50*np.pi/180:
        steer = -50*np.pi/180
    return steer 



# function to inject points in the path recieved from the planning algorithm 
def add_pts(list):
    for i in range(len(list)-1):
        x_mid= (list[i][0]+list[i+1][0])/2
        y_mid= (list[i][1]+list[i+1][1])/2
        list.append(list[i])
        list.append([round(x_mid,3),round(y_mid,3)])
    return list 




#  function to fiind a lookahead point on the path recieved from planning algorithm
def get_goal(path,look_dist):
    #t=path[0:10]
    for i in path:
        a = math.sqrt((i[0])**2 +(i[1])**2)
        if a < look_ahead-2 or a > look_ahead +2:
            pass
            # print(i,a)
        else :
            # print('final',a)
            x_goal=i[0]
            y_goal=i[1]
            break
    p_msg = PointStamped()
    p_msg.header.frame_id = 'base_link'
    p_msg.point.x = x_goal 
    p_msg.point.y = y_goal 
    pub2.publish(p_msg)
    
    return x_goal,y_goal


    
   
#  subscriber callback
def callback(odom,path):

    global steer_list
    carPosx=odom.pose.pose.position.x
    carPosy=odom.pose.pose.position.y
    quaternion = odom.pose.pose.orientation
    (r, p, yaw) = euler_from_quaternion([quaternion.x, quaternion.y, quaternion.z, quaternion.w])
    theta = yaw

    way =[[carPosx,carPosy]] 
    temp=path.data
    
    for i in range(0, len(temp)-1, 2):
        way.append([temp[i], temp[i+1]])
    
    print('check_call')

    added_path=add_pts(way)
    new_path=[]

    for a,i in enumerate(added_path) :
    
        x=i[0]
        y=i[1]
        x_=x-carPosx
        y_=carPosy-y
        x_new=x_*math.cos(theta) - y_*math.sin(theta)
        y_new = -x_*math.sin(theta) - y_*math.cos(theta)
        if x_new > 0:
            new_path.append([x_new,y_new])

    try:
         goal_x,goal_y = get_goal(new_path,look_ahead)
         steer = get_steering(goal_y)
         vel= 14*((math.exp((steer*180/np.pi)/6))/(1+math.exp((steer*180/np.pi)/6))**2)
         if vel<1:
             vel=1.5
         print(vel)
         steer_list.append(steer)
    except :
        steer =steer_list[-1]
        vel=1.5
        print("exception")


    msg = AckermannDriveStamped()
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = '/map'
    msg.drive.steering_angle = steer*2
    msg.drive.speed = vel  #m/s
    pub.publish(msg)



if __name__ == "__main__":
    rospy.init_node("pure_pursuit", anonymous= False)
    pub = rospy.Publisher('/robot_control/command',AckermannDriveStamped , queue_size = 1)         ######### publisher to publish steering and velocity commands to /robot_control/command(topic which which is subscribed by robot_controls node to drive the car)
    odom_sub = message_filters.Subscriber('robot_control/odom', Odometry)                          
    way_sub = message_filters.Subscriber('waypoints_arr', Float64MultiArray)                       ######### subscriber to get the path 
    ts = message_filters.ApproximateTimeSynchronizer([odom_sub, way_sub], 1, 0.1, allow_headerless=True)
    ts.registerCallback(callback)
    rospy.spin()









# ===============velocity generator sample ====================

#   fn = 2*((exp(-25*angle))/(1+exp(-25*angle))**2)
#             speed = self.velocity+fn
#             return speed

# ================= path publisher for visualization ===================

# t_path=Path()
    # t_path.header.stamp=rospy.Time(0)
    # t_path.header.frame_id="base_link"
    # print('33333333333333333333333333333333333333333333333333333333    
    # for a,i in enumerate(new_path):
    #     # print (a)
    #     my_pose = Pose()
    #     my_pose.position.x = i[0]
    #     my_pose.position.y = i[1]
    #     #print('qqqqq',i[0],i[1])
    #     my_pose.position.z = 0
    #     my_pose.orientation.x = 0
    #     my_pose.orientation.y = 0
    #     my_pose.orientation.z = 0
    #     my_pose.orientation.w = 1
    #     pose_stamped = tf2_geometry_msgs.PoseStamped()
    #     pose_stamped.pose = my_pose
    #     pose_stamped.header.frame_id = "base_link"
    #     pose_stamped.header.stamp = rospy.Time(0)
            
    #     t_path.poses.append(pose_stamped)
    # pub3.publish(t_path)
    # print(new_path)