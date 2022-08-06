#! /usr/bin/env python
#coding=utf-8

# Created by Gu

import rospy
from std_msgs.msg import String


def cb():
    rospy.loginfo("节点正在被关闭....")

if __name__ == "__main__":
    # 初始化节点
    """
        作用:ROS初始化
        参数：
            name --- 设置节点名称
            argv=None --- 封装节点调用时传递的参数
            anonymous=False --- 可以为节点名称生成随机后缀，可以解决重名问题
        
    
    """
    rospy.init_node("sanDai",anonymous=True)
    pub = rospy.Publisher("apiPY",String,queue_size=10,latch=True)
    msg = String()
    rate = rospy.Rate(1)
    count = 0
    rospy.sleep(3)
    while not rospy.is_shutdown():
        count += 1
        if count <= 10:
            msg.data = "hello" + str(count)
            pub.publish(msg)
            rospy.loginfo("发布的数据：%s",msg.data)
        else:
            # 关闭节点
            rospy.on_shutdown(cb)
            rospy.signal_shutdown("关闭节点")
        
        rate.sleep()