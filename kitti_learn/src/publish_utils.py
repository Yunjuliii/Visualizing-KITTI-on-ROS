#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import Image,PointCloud2
import sensor_msgs.point_cloud2 as pcl2
from std_msgs.msg import Header
import cv2
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

FRAME_ID = 'map'
def publish_camera(cam_pub,bridge,image):
    cam_pub.publish(bridge.cv2_to_imgmsg(image,"bgr8"))

def publish_point_cloud(pcl_pub,point_cloud):
    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = FRAME_ID
    pcl_pub.publish(pcl2.create_cloud_xyz32(header,point_cloud[:,:3]))

def publish_ego_car(ego_car_pub):
    marker = Marker()
    marker.header.frame_id = FRAME_ID
    marker.action = Marker.ADD
    marker.lifetime = rospy.Duration()
    marker.type = Marker.LINE_STRIP

    marker.color.r = 0.0
    marker.color.g= 0.0
    marker.color.b = 0.0
    marker.color.a = 1.0
    marker.scale.x = 0.2

    marker.points = []
    marker.points.append(Point(10,-10,0))
    marker.points.append(Point(0,0,0))
    marker.points.append(Point(10,10,0))

    ego_car_pub.publish(marker)
 