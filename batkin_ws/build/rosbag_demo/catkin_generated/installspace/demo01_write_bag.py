#!/usr/bin/env python2
#coding=utf-8
# Created by Gu


import rospy
import rosbag
from std_msgs.msg import String
"""
    需求:写出消息数据到磁盘上的bag文件
    流程:
        1.导包;
        2.初始化；
        3.创建rosbag对象并且打开文件流;
        4.写数据;
        5.关闭流。
"""

if __name__ == "__main__":
    rospy.init_node("write_bag")
    bag = rosbag.Bag("hello.bag",'w')
    msg = String()
    msg.data = "hello bag!"
    bag.write("/liaotian",msg)
    bag.write("/liaotian",msg)
    bag.write("/liaotian",msg)
    bag.write("/liaotian",msg)
    bag.write("/liaotian",msg)
    bag.write("/liaotian",msg)
    bag.write("/liaotian",msg)
    bag.close()