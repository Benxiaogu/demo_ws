#! /usr/bin/env python
#coding=utf-8
# Created by Gu


import rospy
import tf2_ros
import math
from tf2_geometry_msgs import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    # 2.初始化
    rospy.init_node("static_sub")
    # 3.创建订阅对象
    # 创建缓存对象
    buffer = tf2_ros.Buffer()
    # 创建订阅对象(将缓存传入)
    sub = tf2_ros.TransformListener(buffer)

    # 创建速度发布对象
    pub = rospy.Publisher("/turtle2/cmd_vel",Twist,queue_size=100)

    # 5.转换逻辑实现,调用tf封装的算法;
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            # ----- 计算 son1 相对于 son2 的坐标关系
            ts = buffer.lookup_transform("turtle2","turtle1",rospy.Time(0))
            rospy.loginfo("父级坐标系:%s,子级坐标系:%s,偏移量(%.2f,%.2f,%.2f)",
                                    ts.header.frame_id,
                                    ts.child_frame_id,
                                    ts.transform.translation.x,
                                    ts.transform.translation.y,
                                    ts.transform.translation.z
                                    )
            # 组织Twist消息
            twist = Twist()
            # 线速度 = 系数 * 坐标系原点的间距 = 系数 * （x^2 + y^2）再开方
            # 角速度 = 系数 * 夹角 = 系数 * atan2(y,x)
            twist.linear.x = 0.5 * math.sqrt(
                math.pow(ts.transform.translation.x,2) + math.pow(ts.transform.translation.y,2))
            twist.angular.z = 4 * math.atan2(ts.transform.translation.y,ts.transform.translation.x)

            # 发布消息
            pub.publish(twist)

        except Exception as e:
            rospy.logwarn("错误提示:%s",e)

        rate.sleep()