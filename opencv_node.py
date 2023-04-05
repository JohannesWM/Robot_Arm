import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2

def image_callback(msg):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv2.imshow("Video Stream", cv_image)
    cv2.waitKey(1)

def display_video():
    rospy.init_node("display_video")
    image_topic = "/camera/image_raw" # Change this to match your video topic
    rospy.Subscriber(image_topic, Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    display_video()
