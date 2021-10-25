import speech_recognition as sr

class RecorderClass():

    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.audio = None
        self.text_recognised = None

    def cancel_noise(self):
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(self.r.energy_threshold))


    def start_record(self):

        with self.m as source:
            self.audio = self.r.listen(source)

        try:
            # recognize speech using Google Speech Recognition
            self.text_recognised = self.r.recognize_google(self.audio, language = 'en-in')
            print(self.text_recognised)

            return (self.text_recognised, 'user')

        except sr.UnknownValueError:
            phrase = "ops! Didn't catch that"
            return (phrase, 'bot')
            print(phrase)

        except sr.RequestError as e:
            phrase = "Uh oh! Couldn't request service!, please check your connectoin;"
            print(phrase)
            return (phrase, 'bot')