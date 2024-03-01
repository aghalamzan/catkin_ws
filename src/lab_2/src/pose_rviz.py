from geometry_msgs.msg import PoseStamped, Quaternion
import rospy
from turtlesim.msg import Pose
from std_msgs.msg import String
import tf

msg = PoseStamped() 

def callback(data):
    global msg
    msg.header.frame_id = "map"
    msg.header.seq = 0
    msg.header.stamp = rospy.Time.now()
    q = tf.transformations.quaternion_from_euler(0, 0, data.theta)
    msg.pose.orientation = Quaternion(*q)
    msg.pose.position.x = data.x
    msg.pose.position.y = data.y

    # Publish the PoseStamped message
    pose_pub.publish(msg)

    # Publish the transform
    br = tf2_ros.TransformBroadcaster()
    t = TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = "turtle_pose"
    t.transform.translation.x = data.x
    t.transform.translation.y = data.y
    t.transform.translation.z = 0.0
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]
    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('pose_listener_python')
    
    # Create a Publisher for PoseStamped messages
    pub = rospy.Publisher('pose_stamped', PoseStamped, queue_size=10)

    # Subscribe to the '/turtle1/pose' topic
    rospy.Subscriber('/turtle1/pose', Pose, callback, queue_size=1)

    # Spin to keep the node running
    rospy.spin()
