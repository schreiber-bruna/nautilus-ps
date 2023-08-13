#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import TransformStamped
import math

def planeta_transformacao(angulo, radianos): 
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "estrela" #coordenada de referencia
    transform.child_frame_id = "planeta" #coordenada q está sendo transformado em relaçao ao de referencia
    transform.transform.translation.x = radianos * math.cos(angulo) #translação ao longo do eixo x
    transform.transform.translation.y = radianos * math.sin(angulo) #translação ao longo do eixo y
    transform.transform.rotation.w = 1.0
    return transform 

def satelite_transformacao(angulo, radianos): 
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "estrela" #coordenada de referencia
    transform.child_frame_id = "satelite" #coordenada q está sendo transformada em relacao ao de referencia
    transform.transform.translation.x = radianos * math.cos(angulo) #translação ao longo do eixo x
    transform.transform.translation.y = radianos * math.sin(angulo) #translação ao longo do eixo y
    transform.transform.rotation.w = 1.0
    return transform

if __name__ == '__main__':
    rospy.init_node('sistema_solar')
    broadcaster = rospy.Publisher('sistema_solar_transformacao', TransformStamped, queue_size=10) #cria um publisher para emviar mensagens fo tipo TRansformStamped para o sistema solar
    rate = rospy.Rate(10)  # 10 Hz

    planeta_radianos = rospy.get_param("~planeta_radianos")
    satelite_radianos = rospy.get_param("~satelite_radianos")

    while not rospy.is_shutdown():
        time = rospy.Time.now() #calcular o angulo q usará na transf

        planeta_angulo = time.to_sec() * math.pi / 5.0 #calcula o angulo no tempo atual para q o angulo varie com o tempo
        planeta_transformacao = planeta_transformacao(planeta_angulo, planeta_radianos)
        broadcaster.publish(planeta_transformacao)

        satelite_angulo = time.to_sec() * math.pi / 2.0
        satelite_transformacao = satelite_transformacao(satelite_angulo, satelite_radianos)
        broadcaster.publish(satelite_transformacao)

        rate.sleep()
