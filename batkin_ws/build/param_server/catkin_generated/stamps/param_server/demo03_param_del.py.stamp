#! /usr/bin/env python2
#coding=utf-8
# Created by Gu

import rospy
"""
    演示参数删除：
        delete_param()

"""

if __name__ == "__main__":
    rospy.init_node("del_param")

    try:
        # 删除参数
        rospy.delete_param("radius_p")
    # except Exception as e:
    except KeyError:
        #如果要删除的参数不存在
        rospy.loginfo("被删除的参数不存在")