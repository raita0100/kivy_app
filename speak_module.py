#import pyttsx3
from plyer import tts
import threading

# engine = pyttsx3.init() # Windows
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-20)

def speak(text):
    # tts.speak(text)
    threading.Thread(
        target = say, args=(text,), daemon=True
    ).start()

def say(text):
    print(text)
    tts.speak(text)

# def say(*text):
#     res = ''
#     for i in text:
#         res+=i
#     print(res)
#     engine.say(res)
# #     engine.runAndWait()
