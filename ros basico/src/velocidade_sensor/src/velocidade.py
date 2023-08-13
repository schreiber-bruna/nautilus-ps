#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Vector3

def velocidade_publisher():
    rospy.init_node('velocidade_publisher', anonymous=True)
    rate = rospy.Rate(1)  # Publica a cada 1 segundo

    velocidade_linear = Vector3(x=1.0, y=2.0, z=3.0)  # Exemplo de vetor de velocidade linear
    velocidade_angular = Vector3(x=0.5, y=0.0, z=0.2)  # Exemplo de vetor de velocidade angular

    linear_pub = rospy.Publisher('velocidade_linear', Vector3, queue_size=10)
    angular_pub = rospy.Publisher('velocidade_angular', Vector3, queue_size=10)

    while not rospy.is_shutdown():
        linear_pub.publish(velocidade_linear)
        angular_pub.publish(velocidade_angular)
        rate.sleep()

if __name__ == '__main__':
    try:
        velocidade_publisher()
    except rospy.ROSInterruptException:
        pass
