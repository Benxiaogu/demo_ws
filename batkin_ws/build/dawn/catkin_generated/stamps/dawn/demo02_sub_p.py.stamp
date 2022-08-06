#! /usr/bin/env python2
#coding=utf-8

# Created by Gu

import rospy
from std_msgs.msg import String



"""
    订阅实现流程：
    1.导包；
    2.初始化ROS节点;
    3.创建订阅者对象；
    4.回调函数处理数据；
    5.spin()
"""

def doMsg(msg):
    # 回调函数
    rospy.loginfo("我订阅的数据:%s",msg.data)


if __name__ == "__main__":
    rospy.init_node("study2")
    sub = rospy.Subscriber("che",String,doMsg,queue_size=10)
    rospy.spin()
