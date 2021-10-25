from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from recordmodule import RecorderClass

from initialisemodule import Initialise
from endmodule import EndConversation

import scrapingmodule as find_answer
import speak_module
import time

global coversation_messages

coversation_messages = []



class SearchClass():
    serch_text = "Searching For Results..."


class BotSection(ScrollView):
    pass

class UserSection(ScrollView):
    pass


class OparationSection(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("\n\nMaintain Silence : \n\n")
        self.rc = RecorderClass()
        self.rc.cancel_noise()


    def start_session(self):
        self.parent.ids.botsec.children[0].text = Initialise().welcome_msg
        self.parent.ids.usersec.children[0].text = "Your Query"
        Initialise().greet()

    def end_conversation(self):
        global coversation_messages
        self.parent.ids.botsec.children[0].text = EndConversation().end_msg
        EndConversation().package_and_mail(coversation_messages)

    def record(self):
        global coversation_messages

        #self.children[1].canvas.before.children[0].source = "assets/images/voice_on.png"

        print("Recording....")
        data = self.rc.start_record()

        #self.children[1].canvas.before.children[0].source = "assets/images/voice.png"

        if data[1] == 'bot':
            self.parent.ids.botsec.children[0].text = data[0]
            find_answer.sleep(1)
            speak_module.speak(data[0])
            return

        self.parent.ids.usersec.children[0].text = data[0]

        self.parent.ids.botsec.children[0].text = SearchClass().serch_text

        speak_module.speak(SearchClass().serch_text)

        ans = find_answer.scrape_data(data[0])

        disp_text = ''
        for i in range(len(ans)):
            disp_text += ans[i]
            disp_text += '\n'
            if i >= 5:
                break
        self.parent.ids.botsec.children[0].text = str(disp_text)

        find_answer.sleep(1)
        speak_module.speak(ans[0])

        coversation_messages.append(
            {
                'user': data[0],
                'bot': ans
            }
        )


class InformationSection(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def copy_phone(self, text):
        try:
            from kivy.core.clipboard import Clipboard
            Clipboard.copy(text)
        except:
            print("Could not be copied to clipboard: " + text)
            pass

    def copy_mail(self, text):
        try:
            from kivy.core.clipboard import Clipboard
            Clipboard.copy(text)
        except:
            print("Could not be copied to clipboard: " + text)
            pass

class MainWidgetSection(GridLayout):
    pass

class TheLabApp(App):
    pass


app = TheLabApp()
app.run()