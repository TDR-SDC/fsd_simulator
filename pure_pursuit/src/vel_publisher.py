import rospy
from geometry_msgs.msg import Twist

def callback(data):
    msg = Twist()
    msg.angular = data.angular
    msg.linear.x = 4
    msg.angular.y=0.5
    pub.publish(msg)

if __init__ == '__main__':
    rospy.init_node('vel_publisher')
    pub = rospy.Publisher('cmd_vel', Twist)
    sub = rospy.Subscriber('cmd_vel', Twist, callback)