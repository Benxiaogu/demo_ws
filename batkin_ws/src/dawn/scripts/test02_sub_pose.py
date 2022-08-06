#! /usr/bin/env python
#coding=utf-8

# Created by Gu


import rospy
from turtlesim.msg import Pose
"""
    需求：订阅并输出乌龟位姿信息

"""

def doPose(pose):
    rospy.loginfo(
        "P->乌龟位姿信息：坐标(%.2f,%.2f),朝向：%.2f,线速度:%.2f,角速度:%.2f",
        pose.x,pose.y,pose.theta,pose.linear_velocity,pose.angular_velocity)

if __name__ == "__main__":
    rospy .init_node("sub_pose")
    sub = rospy.Subscriber("/turtle1/pose",Pose,doPose,queue_size=100)
    rospy.spin()