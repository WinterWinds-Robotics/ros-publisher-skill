from mycroft import MycroftSkill, intent_file_handler
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class RosPublisher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.node = rclpy.create_node('mycroft_pub')
        self.pub = self.node.create_publisher(String, "/mycroft", 1)

    @intent_file_handler('publisher.ros.intent')
    def handle_publisher_ros(self, message):
        self.speak_dialog('publisher.ros')
        msg = String()
        msg.data = message.data.get('utterance')
        self.pub.publish(msg)

def create_skill():
    return RosPublisher()



