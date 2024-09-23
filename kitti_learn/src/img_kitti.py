#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import os
import cv2
from cv_bridge import CvBridge

DATA_PATH='/home/lyj/data/kitti/RawData/2011-09-26/2011_09_26_drive_0005_sync'

if __name__ == '__main__':
    frame = 0
    rospy.init_node('kitti_image',anonymous=True)
    cam_pub = rospy.Publisher('Image_pub',Image,queue_size=10)
    rate = rospy.Rate(10)
    bridge = CvBridge()
    while not rospy.is_shutdown():
        img_path = os.path.join(DATA_PATH,'image_02/data/%010d.png'%frame)
        img = cv2.imread(img_path)
        ros_image = bridge.cv2_to_imgmsg(img,'bgr8')
        cam_pub.publish(ros_image)
        rospy.loginfo('image published')
        rate.sleep()
        frame +=1
        frame %=154


