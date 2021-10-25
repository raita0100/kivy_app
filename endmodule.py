import speak_module
from mail_module import Mail

global mail_object

mail_object = Mail()

class EndConversation():

    end_msg = "Thank you!, For using the service. Your Conversation will me mailed to authority."


    def package_and_mail(self, conversation_messages):
        global mail_object

        body = self.get_proper_str(conversation_messages)

        mail_object.send_message('conversation', str(conversation_messages))

        speak_module.speak(self.end_msg)

    def get_proper_str(self, list_msgs):

        conv = "{"

        print(list_msgs)
        for i in list_msgs:
            data = {}
            data['user'] = i['user']
            data['bot'] = ""
            for ii in i['bot']:
                try:

                    data['bot'].join(c for c in ii if ord(c) < 128)
                    data['bot'] += '\n'

                except Exception as e:
                    print(f"Exception occured at :\n{ii}\n\n ")

            conv += str(data) + ","
        conv += "}"
        return conv