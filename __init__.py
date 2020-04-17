from mycroft import MycroftSkill, intent_file_handler


class FirstPicroft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('picroft.first.intent')
    def handle_picroft_first(self, message):
        self.speak_dialog('picroft.first')


def create_skill():
    return FirstPicroft()

