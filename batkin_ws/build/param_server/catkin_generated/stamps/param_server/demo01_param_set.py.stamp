#! /usr/bin/env python2
#coding=utf-8
# Created by Gu


import rospy

"""
    演示参数的新增与修改：
    需求：在参数服务器中设置机器人属性，型号，半径
    实现：
        rospy.set_param()

"""
if __name__ == "__main__":
    rospy.init_node("study5")
    rospy.set_param("type_p","xiaohuangche")
    rospy.set_param("radius_p",0.15)
    # 修改参数，覆盖掉之前的参数值
    rospy.set_param("radius_p",0.2)