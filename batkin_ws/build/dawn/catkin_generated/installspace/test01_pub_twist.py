#!/usr/bin/env python2
#coding=utf-8

# Created by Gu


import rospy
from geometry_msgs.msg import Twist

"""
    发布方：发布速度消息
        话题:/turtle1/cmd_vel
        消息:geometry_msgs/Twist
"""



if __name__ == "__main__":
    rospy.init_node("my_control_p")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    rate = rospy.Rate(10)
    twist = Twist()
    twist.linear.x = 1
    twist.linear.y = 0
    twist.linear.z = 0

    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = 1


    while not rospy.is_shutdown():
        pub.publish(twist)
        rate.sleep()
