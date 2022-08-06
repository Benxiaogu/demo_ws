#!/usr/bin/env python2
#coding=utf-8

## Created by xiaogu

import rospy

if __name__ == "__main__":
	# 初始化ROS节点
	rospy.init_node("hello")
	# 输出日志
	rospy.loginfo("hello world!")
