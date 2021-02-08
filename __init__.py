from mycroft import MycroftSkill, intent_file_handler
from mycroft import FallbackSkill
from mycroft.messagebus.message import Message

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class RosPublisher(FallbackSkill):
    def __init__(self):
        super().__init__()
        rclpy.init()
        self.node = rclpy.create_node('mycroft_publisher_skill')
        self.pub = self.node.create_publisher(String, "/mycroft_skill", 1)

    def initialize(self):
        self.add_event('recognizer_loop:utterance', self.publish_to_ros)
        self.register_fallback(self.publish_to_ros, 1)

    def publish_to_ros(self, message):
        utt = message.data.get('utterance')
        if utt is  not None:
            self.log.info('ROS Publisher {}'.format(utt))
            msg = String()
            msg.data = utt
            self.pub.publish(msg)
    
    def shutdown(self):
        self.node.destroy_node()
        rclpy.shutdown()
    def __del__(self):
        rclpy.shutdown()

def create_skill():
    return RosPublisher()



