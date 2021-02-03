from mycroft import MycroftSkill, intent_file_handler


class RosPublisher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('publisher.ros.intent')
    def handle_publisher_ros(self, message):
        self.speak_dialog('publisher.ros')


def create_skill():
    return RosPublisher()

