#! /usr/bin/env python2
#coding=utf-8

# Created by Gu


import rospy
from dawn.msg import Person

"""
    订阅方：订阅人的消息
        1.导包；
        2.初始化ROS节点;
        3.创建订阅者对象；
        4.处理订阅的数据；
        5.spin()。
"""


def doPerson(p):
    rospy.loginfo("小伙子的数据：%s,%d,%.2f",p.name,p.age,p.height)

if __name__ == "__main__":
    rospy.init_node("study_3")
    sub = rospy.Subscriber("tian",Person,doPerson)
    rospy.spin()