#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float64

def velocidade_subscriber():
    rospy.init_node('velocidade_subscriber', anonymous=True)

    def linear_callback(data):
        modulo_linear = (data.x ** 2 + data.y ** 2 + data.z ** 2) ** 0.5 #calcula o modulo do vetor da variável data
        modulo_linear_pub.publish(modulo_linear)

    def angular_callback(data):
        modulo_angular = (data.x ** 2 + data.y ** 2 + data.z ** 2) ** 0.5 #calcula o modulo do vetor da variável data
        modulo_angular_pub.publish(modulo_angular)

    rospy.Subscriber('velocidade_linear', Vector3, linear_callback) # o nó se inscreve em velocidade_linear para receber as mensagem publicadas nele, o Vector3 é o tipo de mensagem q ele está esperando receber
    rospy.Subscriber('velocidade_angular', Vector3, angular_callback)

    linear_module_pub = rospy.Publisher('modulo_linear', Float64, queue_size=10) #modulo_linear é o tópico q o publisher publica as mensagens, Float64 é o tipo de mensagem q o publisher envia
    angular_module_pub = rospy.Publisher('modulo_angular', Float64, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    try:
        velocidade_subscriber()
    except rospy.ROSInterruptException:
        pass
