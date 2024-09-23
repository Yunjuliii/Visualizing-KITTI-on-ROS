#!/usr/bin/env python3
import rospy
from data_utils import *
from publish_utils import *
import os
from geometry_msgs.msg import Point
from cv_bridge import CvBridge

DATA_PATH='/home/lyj/data/kitti/RawData/2011-09-26/2011_09_26_drive_0005_sync'

if __name__ == '__main__':
    frame = 0
    rospy.init_node('kitti_image',anonymous=True)
    cam_pub = rospy.Publisher('Image_pub',Image,queue_size=10)
    pcl_pub = rospy.Publisher('kitti_point_cloud',PointCloud2,queue_size = 10)
    ego_pub = rospy.Publisher('kitti_ego_car',Marker,queue_size=10)
    rate = rospy.Rate(10)
    bridge = CvBridge()
    while not rospy.is_shutdown():
        image = read_camera(os.path.join(DATA_PATH,'image_02/data/%010d.png'%frame))
        publish_camera(cam_pub,bridge,image)
        point_cloud = read_point_cloud(os.path.join(DATA_PATH,'velodyne_points/data/%010d.bin'%frame))
        publish_point_cloud(pcl_pub,point_cloud)           
        publish_ego_car(ego_pub)
        rospy.loginfo('image and cloud published')
        rate.sleep()
        frame +=1
        frame %=154


