#! /usr/bin/env python2
#coding=utf-8
# Created by Gu


import rospy
from server_client.srv import AddInts,AddIntsRequest,AddIntsResponse
"""
    服务端：解析客户端请求，产生响应。
        1.导包；
        2.初始化ROS节点;
        3.创建服务端对象；
        4.处理逻辑（回调函数）；
        5.spin()。
"""
# 回调函数：返回值便是响应数据
def doNum(request):
    num1 = request.num1
    num2 = request.num2
    sum = num1 + num2
    response = AddIntsResponse()
    response.sum = sum

    rospy.loginfo(
        "服务器解析的数据num1=%d,num2=%d,响应的结果:sum=%d",num1,num2,sum
        )
    return response

if __name__ == "__main__":
    rospy.init_node("study4")
    server = rospy.Service("addInts",AddInts,doNum)
    rospy.loginfo("服务器已经启动了")
    rospy.spin()