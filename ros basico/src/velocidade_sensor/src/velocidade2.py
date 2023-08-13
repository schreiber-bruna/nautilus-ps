#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float64

def velocidade_subscriber():
    rospy.init_node('velocity_subscriber', anonymous=True)

    def linear_callback(data):
        modulo_linear = (data.x ** 2 + data.y ** 2 + data.z ** 2) ** 0.5
        modulo_linear_pub.publish(modulo_linear)

    def angular_callback(data):
        modulo_angular = (data.x ** 2 + data.y ** 2 + data.z ** 2) ** 0.5
        modulo_angular_pub.publish(modulo_angular)

    rospy.Subscriber('velocidade_linear', Vector3, linear_callback)
    rospy.Subscriber('velocidade_angular', Vector3, angular_callback)

    linear_module_pub = rospy.Publisher('modulo_linear', Float64, queue_size=10)
    angular_module_pub = rospy.Publisher('modulo_angular', Float64, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    try:
        velocidade_subscriber()
    except rospy.ROSInterruptException:
        pass
