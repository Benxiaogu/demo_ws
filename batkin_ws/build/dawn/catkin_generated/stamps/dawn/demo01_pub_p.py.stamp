#! /usr/bin/env python2
#coding=utf-8

# Created by Gu

import rospy
from std_msgs.msg import String   # 发布的消息的类型
import tools

"""
    使用python实现消息实现:
        1.导包；
        2.初始化ros节点;
        3.创建发布者对象；
        4.编写发布逻辑并发布数据。
"""



if __name__ == "__main__":

    rospy.init_node("study1")
    rospy.loginfo("num = %d",tools.num)
    pub = rospy.Publisher("che",String,queue_size=10)
    msg = String()

    # 指定发布频率
    rate = rospy.Rate(1)

    count = 0

    rospy.sleep(3)
    while not rospy.is_shutdown():
        count += 1
        msg.data = "hello" + str(count)
        pub.publish(msg)
        rospy.loginfo("发布的数据:%s",msg.data)
        rate.sleep()

