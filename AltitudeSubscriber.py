import rospy
from std_msgs.msg import Float64
 
def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "Altitude is %f", data.data)
      
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("global_position/rel_alt", Float64, callback)
	rospy.spin()
 
if __name__ == '__main__':
	listener()