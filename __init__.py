from mycroft import MycroftSkill, intent_file_handler
import rospy

class RosPublisher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        rospy.init_node('mycroft_node', log_level=rospy.DEBUG, disable_signals=True)

    @intent_file_handler('publisher.ros.intent')
    def handle_publisher_ros(self, message):
        self.speak_dialog('publisher.ros')
        rospy.loginfo(message)


def create_skill():
    return RosPublisher()

