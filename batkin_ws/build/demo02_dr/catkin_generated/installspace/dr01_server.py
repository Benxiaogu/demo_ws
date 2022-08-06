#!/usr/bin/env python2
# coding=utf-8
# Created by Gu

import rospy
from dynamic_reconfigure.server import Server
from demo02_dr.cfg import drConfig

def cb(drConfig,level):
    rospy.loginfo("解析的参数:%d,%.2f,%s,%d,%d",
                            drConfig.int_param,
                            drConfig.double_param,
                            drConfig.str_param,
                            drConfig.bool_param,
                            drConfig.list_param,
                            )
    return drConfig

if __name__ == "__main__":
    rospy.init_node("dr_server")
    # Server(type, callback, namespace="")
    # type类型  callback回调函数
    server = Server(drConfig,cb)
    rospy.spin()