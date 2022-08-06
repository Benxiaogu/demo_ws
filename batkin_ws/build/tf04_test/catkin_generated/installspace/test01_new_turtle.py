#!/usr/bin/env python2
#coding=utf-8
# Created by Gu



import rospy
from turtlesim.srv import Spawn,SpawnRequest,SpawnResponse

"""
    需求：向服务器发送请求生成一只乌龟
        话题:/Spawn
        消息:turtlesim/Spawn

"""
if __name__ == "__main__":
    rospy.init_node("service_call")
    client = rospy.ServiceProxy("/spawn",Spawn)
    # 组织数据
    request = SpawnRequest()
    request.x =3.5
    request.y = 2.0
    request.theta = -3
    request.name = "turtle2"
    # 判断服务器状态并发送
    client.wait_for_service()
    try:
        response = client.call(request)
        rospy.loginfo("生成乌龟的名字叫:%s",response.name)
    except Exception as e:
        rospy.logerr("请求处理异常")