#!/usr/bin/env python2
#coding=utf-8

# Created by Gu


import rospy

if __name__ == "__main__":
    # 演示日志函数
    rospy.init_node("hello_log")
    rospy.logdebug("DEBUG消息...")
    rospy.loginfo("INFO消息...")
    rospy.logwarn("WARN消息...")
    rospy.logerr("ERROR消息...")
    rospy.logfatal("FATAL消息...")