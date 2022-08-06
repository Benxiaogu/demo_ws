#! /usr/bin/env python2
#coding=utf-8

# Created by Gu

import rospy
from dawn.msg import Person
"""
    发布方：发布人的消息
        1.导包；
        2.初始化ROS节点;
        3.创建发布者对象；
        4.组织发布逻辑并发布数据。
"""


if __name__ == "__main__":
    rospy.init_node("study3")
    pub = rospy.Publisher("tian",Person,queue_size=10)
    p = Person()
    p.name = "奥特曼"
    p.age = 18
    p.height = 1.85
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(p)
        rospy.loginfo("发布的消息:%s,%d,%.2f",p.name,p.age,p.height)
        rate.sleep()