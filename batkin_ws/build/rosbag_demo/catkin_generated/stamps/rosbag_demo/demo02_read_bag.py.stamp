#! /usr/bin/env python
#coding=utf-8
# Created by Gu
import rospy
import rosbag

"""
    需求:读取磁盘上的bag文件
"""
if __name__ == "__main__":
    rospy.init_node("read_bag")
    bag = rosbag.Bag("hello.bag",'r')
    msgs = bag.read_messages("/liaotian")
    for topic,msg,time in msgs:
        rospy.loginfo("话题:%s,消息:%s,时间:%s",topic,msg.data,time)
    bag.close()