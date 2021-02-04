from mycroft import MycroftSkill, intent_file_handler
import rospy
from std_msgs.msg import String

class RosPublisher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        rospy.init_node('mycroft_node', log_level=rospy.DEBUG, disable_signals=True)
        self.pub = rospy.Publisher("/mycroft", String, queue_size=1)

    @intent_file_handler('publisher.ros.intent')
    def handle_publisher_ros(self, message):
        self.speak_dialog('publisher.ros')
        self.pub.publish(message)


def create_skill():
    return RosPublisher()
