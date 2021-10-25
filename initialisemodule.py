import speak_module

class Initialise():
    welcome_msg = "Welcome! Please ask your query?"

    def greet(self):
        speak_module.speak(self.welcome_msg)
