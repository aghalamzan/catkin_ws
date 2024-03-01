#!/usr/bin/env python

import rospy
import random
from turtlesim.srv import Spawn, TeleportAbsolute

def spawn_and_teleport_turtle():
    rospy.init_node('spawn_and_teleport_turtle_node', anonymous=True)
    
    # Define the service proxies
    spawn_client = rospy.ServiceProxy('/spawn', Spawn)
    teleport_client = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
    
    # Loop at 1 Hz
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        # Generate random position and angle
        x_pos = random.uniform(1, 10)  # Adjust the range as needed
        y_pos = random.uniform(1, 10)  # Adjust the range as needed
        theta = random.uniform(0, 2 * 3.14159)  # Adjust the range as needed

        # Spawn a new turtle
        spawn_client(x_pos, y_pos, theta, "random_turtle")

        # Teleport the turtle to a random position
        teleport_client(x_pos, y_pos, theta)

        # Sleep to maintain 1 Hz rate
        rate.sleep()

if __name__ == '__main__':
    try:
        spawn_and_teleport_turtle()
    except rospy.ROSInterruptException:
        pass

