#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

import rospy 
import std_msgs

rospy.init_node("wireless_check")
pub = rospy.Publisher("wifi_connected", std_msgs.msg.Bool, queue_size=1)

def check_wireless(devname):
    t = os.popen('iw dev %s info' % devname)
    f = t.read()
    if f.find('ssid') > 0:
        msg = std_msgs.msg.Bool()
        msg.data = True
        pub.publish(msg)

if __name__ == "__main__":
    r = rospy.Rate(0.5)
    while True:
        check_wireless('wlp4s0')
        r.sleep()