#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import TransformStamped
import math

def planeta_transformacao(angle, radius): 
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "estrela"
    transform.child_frame_id = "planeta"
    transform.transform.translation.x = radius * math.cos(angle)
    transform.transform.translation.y = radius * math.sin(angle)
    transform.transform.rotation.w = 1.0
    return transform

def satelite_transformacao(angle, radius): 
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "estrela"
    transform.child_frame_id = "satelite"
    transform.transform.translation.x = radius * math.cos(angle)
    transform.transform.translation.y = radius * math.sin(angle)
    transform.transform.rotation.w = 1.0
    return transform

if __name__ == '__main__':
    rospy.init_node('sistema_solar')
    broadcaster = rospy.Publisher('sistema_solar_transform', TransformStamped, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    planeta_radianos = rospy.get_param("~planeta_radianos")
    satelite_radianos = rospy.get_param("~satelite_radianos")

    while not rospy.is_shutdown():
        time = rospy.Time.now()

        planeta_angulo = time.to_sec() * math.pi / 5.0
        planeta_transformacao = planeta_transformacao(planeta_angulo, planeta_radianos)
        broadcaster.publish(planeta_transformacao)

        satelite_angulo = time.to_sec() * math.pi / 2.0
        satelite_transformacao = satelite_transformacao(satelite_angulo, satelite_radianos)
        broadcaster.publish(satelite_transformacao)

        rate.sleep()
