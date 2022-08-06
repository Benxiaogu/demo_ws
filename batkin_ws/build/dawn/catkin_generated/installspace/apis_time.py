#!/usr/bin/env python2
#coding=utf-8

# Created by Gu


import rospy

"""
    需求1:演示时间相关操作（获取当前时刻+设置指定时刻）
    需求2:程序执行中停顿5秒
    需求3:获取程序开始执行的时刻，且已知持续运行的时间，计算程序结束的时间
    需求4:创建定时器,实现类似于rospy.Rate的功能(间隔某个时间间隔执行某种操作)
"""

def doMsg(event):
    rospy.loginfo("++++++++++++++")
    rospy.loginfo("调用回调函数的时刻:%.2f",event.current_real.to_sec())

if __name__ == "__main__":
    rospy.init_node("hello_time")
    # 需求1:演示时间相关操作（获取当前时刻+设置指定时刻）
    # 获取时刻
    time_now = rospy.Time.now()  # 获取当前时刻并封装成对象
    rospy.loginfo("当前时刻:%.2f",time_now.to_sec())
    rospy.loginfo("当前时刻:%d",time_now.secs)
    # 设置指定
    time1 = rospy.Time(100.5)  # 将时间(1970年01月01日00:00:00逝去100.5秒)封装成Time对象
    time2 = rospy.Time(100,312345678)# 将时间(1970年01月01日00:00:00逝去100.312345678秒)封装成Time对象
    rospy.loginfo("指定时刻1:%.2f",time1.to_sec())
    rospy.loginfo("指定时刻2:%.2f",time2.to_sec())

    # 从某个时间值获取时间对象
    time3 = rospy.Time.from_sec(210.12)
    rospy.loginfo("指定时刻3:%.2f",time3.to_sec())

    # 需求2:程序执行中停顿5秒
    rospy.loginfo("休眠前---------------")
    t1 = rospy.Time.now()
    # 1.封装一个持续时间对象（5秒）
    du = rospy.Duration(5)
    # 2.再将持续时间休眠
    rospy.sleep(du)
    t2 = rospy.Time.now()
    rospy.loginfo("休眠后---------------")
    t = t2.to_sec() - t1.to_sec()
    rospy.loginfo("休眠时间:%.2fs",t)

    # 需求3:获取程序开始执行的时刻，且已知持续运行的时间，计算程序结束的时间
    # 1.获取一个时刻t_1
    t_1 = rospy.Time.now()
    # 2.设置一个持续时间du_1
    du_1 = rospy.Duration(5)
    # 3.结束时刻t_2 = t_1 + du_1
    t_2 = t_1 + du_1
    rospy.loginfo("开始时刻:%.2f",t_1.to_sec())
    rospy.loginfo("结束时刻:%.2f",t_2.to_sec())

    du_2 = du + du_1
    rospy.loginfo("持续时间相加:%.2f",du_2.to_sec())

    # 需求4:创建定时器,实现类似于rospy.Rate的功能(间隔某个时间间隔执行某种操作)
    # timer = rospy.Timer(rospy.Duration(2),doMsg,True)  # 创建一个定时器对象
    timer = rospy.Timer(rospy.Duration(2),doMsg)
    rospy.spin()

