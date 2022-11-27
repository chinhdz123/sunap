from datetime import date, datetime
import os
from mypackage.speak_hear import *
from mymodule.talk import *
speak("Hello boss, can i help you?")
d = date.today().strftime("%B %d, %Y")
now = datetime.now()
while True:
    you = hear()
    if you is None:
        speak("i can't hear you, please say again, boss")
    elif "today" in you and "what" in you:
        speak("today is " + d)
    elif "what" and "time" in you:
        speak("it's " + now.strftime("%H %M"))
    elif "my" in you and "profile":
        os.startfile("D:\chinh")
    elif "goodbye" in you:
        speak("goodbye boss")
        exit()
    elif "hold on" in you:
        speak("enter any press to continue")
        input()
    elif "talk" in you:
        talk()

