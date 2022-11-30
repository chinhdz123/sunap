from datetime import datetime
import pyttsx3
import speech_recognition as sr
import playsound
from gtts import gTTS
import os


def hear():
    print("Michael:Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Boss: ", end='')
        audio = r.listen(source, phrase_time_limit=3)  # nghe
        try:
            text = r.recognize_google(audio, language="vi")  # dịch ra
            print(text)
            return str(text).lower()
        except:
            return None


def speak(text):
    pass
    # print("Michael: " + text)
    # engine = pyttsx3.init()
    # voice = engine.getProperty("voices")
    # engine.setProperty("voice", voice[1].id)
    # engine.say(text)
    # engine.runAndWait()
    """ date_string = datetime.now().strftime("%d")
    tts = gTTS(text=text, lang = "vi")
    filename = "voice"+date_string +".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename) """
