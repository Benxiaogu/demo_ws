#!/usr/bin/env python2
#coding=utf-8

# Created by Gu

import rospy
"""
    需求:修改乌龟GUI的背景色


"""

if __name__ == "__main__":
    rospy.init_node("change_color")
    rospy.set_param("/turtlesim/background_r",120)
    rospy.set_param("/turtlesim/background_g",60)
    rospy.set_param("/turtlesim/background_b",200)
