#! /usr/bin/env python
#coding=utf-8

## Created by xiaogu

# 导包
import rospy

if __name__ == "__main__":
    # 初始化ros节点
    rospy.init_node("hello_p")
    # 输出日志
    rospy.loginfo("hello vscode!")
