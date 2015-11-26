#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

last_msg = None

def callback(msg):
  t = Twist()
  t.linear.x = msg.axes[1]
  t.angular.z = msg.axes[0]  
  global last_msg
  last_msg = t

if __name__ == "__main__":
  rospy.init_node('turtlejoy', anonymous=True)
  publisher = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
  s = rospy.Subscriber("joy", Joy, callback)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    if not last_msg == None:
      publisher.publish(last_msg)
      last_msg = None
    rate.sleep()
  

